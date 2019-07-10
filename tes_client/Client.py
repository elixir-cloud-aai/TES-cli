"""
Client script for the mock Task Execution Service
"""
from bravado.client import SwaggerClient
from bravado_core.formatter import DEFAULT_FORMATS


# specify config for bravado
DEFAULT_CONFIG = {
    "validate_requests": False,
    "validate_responses": False,
    "headers": None,
    "formats": DEFAULT_FORMATS["int64"],
}

# define a clinet
class Client:
    def __init__(self, url, config=DEFAULT_CONFIG):
        self._config = config
        config["formats"] = [DEFAULT_FORMATS["int64"]]
        swagger_path = "{}/swagger.json".format(url.rstrip("/"))

        self.models = SwaggerClient.from_url(swagger_path, config=config)
        self.client = self.models.TaskService

    # to-do :
    #   remove the DefineTask function and leave ListTasks blank
    def DefineTask(self, task_id):
        tesTask = self.models.get_model("tesTask")
        tesExecutor = self.models.get_model("tesExecutor")
        # to-implement
        t1 = tesExecutor(image="", command=[])
        t2 = tesExecutor(image="", command=[])
        return tesTask(id=task_id, executors=[t1, t2])

    def ListTasks(self, name_prefix, page_size, page_token, view="BASIC"):
        return self.client.ListTasks(
            view=view,
            name_prefix=name_prefix,
            page_size=page_size,
            page_token=page_token,
        ).result()

    def GetServiceInfo(self):
        return self.client.GetServiceInfo().result()

    def GetTaskInfo(self, cpu_cores, ram_gb, disk_gb, preemptible, zones, execution_time_min):
        tesResources = self.models.get_model("tesResources")
        request = tesResources(
            cpu_cores=cpu_cores,
            ram_gb=ram_gb,
            disk_gb=disk_gb,
            preemptible=preemptible,
            zones=zones,
            execution_time_min=execution_time_min
        )
        # to-do :
        #   validate response
        return self.client.GetTaskInfo(body=request).result()

    def GetTask(self, task_id):
        return self.client.GetTask(id=task_id).result()

    def CreateTask(self, task_id):
        return self.client.CreateTask(body=self.DefineTask(task_id)).result()

    def CancelTask(self, task_id):
        return self.client.CancelTask(id=task_id).result()


if __name__ == "__main__":

    # an example of how to use the client
    client = Client(url="http://0.0.0.0:9001/ga4gh/tes/v1")

    response = client.GetTaskInfo(
        cpu_cores=4, ram_gb=8, disk_gb=100, preemptible=True, zones=[], execution_time_min=10
    )
    print(response)
