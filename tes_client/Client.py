"""
Client script for the mock Task Execution Service
"""
from bravado.client import SwaggerClient
from bravado_core.formatter import DEFAULT_FORMATS

# Bravado configuration
DEFAULT_CONFIG = {
    "validate_requests": False,
    "validate_responses": False,
    "headers": None,
    "formats": [DEFAULT_FORMATS["int64"]],
}


class Client:
    '''Client for mock-TES service.'''
    def __init__(self, url, config=DEFAULT_CONFIG):
        swagger_path = "{url}/swagger.json".format(url=url.rstrip("/"))
        self.models = SwaggerClient.from_url(
            swagger_path,
            config=config
        )
        self.client = self.models.TaskService

    def GetTaskInfo(
        self,
        cpu_cores,
        ram_gb,
        disk_gb,
        preemptible,
        zones,
        execution_time_min
    ):
        # TODO: validate response
        tesResources = self.models.get_model("tesResources")
        request = tesResources(
            cpu_cores=cpu_cores,
            ram_gb=ram_gb,
            disk_gb=disk_gb,
            preemptible=preemptible,
            zones=zones,
            execution_time_min=execution_time_min
        )
        return self.client.GetTaskInfo(body=request).result()

    def UpdateTaskInfoConfig(
        self,
        currency,
        time_unit,
        unit_costs,
    ):
        tesTaskInfoConfig = self.models.get_model("tesTaskInfoConfig")
        request = tesTaskInfoConfig(
            currency=currency,
            time_unit=time_unit,
            unit_costs={
                "cpu_usage": unit_costs["cpu_usage"],
                "memory_consumption": unit_costs["memory_consumption"],
                "data_storage": unit_costs["data_storage"],
                "data_transfer": unit_costs["data_transfer"],
            }
        )
        return self.client.UpdateTaskInfoConfig(body=request).result()
