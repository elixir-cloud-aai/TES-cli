"""
Client for the mockup GA4GH Task Execution Service `mock-TES`.
"""
from urllib.parse import urlparse

from bravado.client import SwaggerClient
from bravado_core.formatter import DEFAULT_FORMATS
from bravado.requests_client import RequestsClient

# Bravado configuration
DEFAULT_CONFIG = {
    "validate_requests": False,
    "validate_responses": False,
    "headers": None,
    "formats": [DEFAULT_FORMATS["int64"]],
    "include_missing_properties": True,
}


class Client:
    """Client for mock-TES service."""
    def __init__(
        self,
        url,
        jwt=None,
        config=DEFAULT_CONFIG
    ):
        swagger_path = "{url}/swagger.json".format(url=url.rstrip("/"))
        if jwt:
            http_client = RequestsClient()
            http_client.set_api_key(
                host=urlparse(url).netloc,
                api_key=f"Bearer {jwt}",
                param_name="Authorization",
                param_in="header"
            )
        else:
            http_client = None
        self.models = SwaggerClient.from_url(
            swagger_path,
            config=config
        )
        self.client = self.models.TaskService


    def getTaskInfo(
        self,
        timeout: float = 3,
        **kwargs,
    ):
        tesResources = self.models.get_model("tesResources")
        request = tesResources(
            **kwargs,
        )
        return self.client.GetTaskInfo(
            body=request
        ).result(timeout=timeout)


    def updateTaskInfoConfig(
        self,
        currency,
        unit_costs,
        timeout: float = 3,
    ):
        tesTaskInfoConfig = self.models.get_model("tesTaskInfoConfig")
        request = tesTaskInfoConfig(
            currency=currency,
            unit_costs={
                "cpu_usage": unit_costs["cpu_usage"],
                "memory_consumption": unit_costs["memory_consumption"],
                "data_storage": unit_costs["data_storage"],
                "data_transfer": unit_costs["data_transfer"],
            }
        )
        return self.client.UpdateTaskInfoConfig(
            body=request
        ).result(timeout=timeout)
