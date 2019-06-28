"""
Client script for the mock Task Execution Service
"""
from bravado.client import SwaggerClient
from bravado_core.formatter import DEFAULT_FORMATS


# connexion stub runs on port 5000 and the schema is available at this endpoint
connexion_url = "http://127.0.0.1:8888/ga4gh/tes/v1"

# specify config for bravado
DEFAULT_CONFIG = {
    "validate_requests": False,
    "validate_responses": False,
    "headers": None,
    "formats": DEFAULT_FORMATS["int64"],
}

# define a clinet
class Client:
    def __init__(self, url=connexion_url, config=DEFAULT_CONFIG):
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

    def GetServiceInfoTaskInfo(self, cpu_cores, ram_gb, disk_gb, preemptible, zones):
        tesResources = self.models.get_model("tesResources")
        request = tesResources(
            cpu_cores=cpu_cores,
            ram_gb=ram_gb,
            disk_gb=disk_gb,
            preemptible=preemptible,
            zones=zones
        )
        # to-do :
        #   validate response
        return self.client.GetServiceInfoTaskInfo(body=request).result()

    def GetTask(self, task_id):
        return self.client.GetTask(id=task_id).result()

    def CreateTask(self, task_id):
        return self.client.CreateTask(body=self.DefineTask(task_id)).result()

    def CancelTask(self, task_id):
        return self.client.CancelTask(id=task_id).result()


if __name__ == "__main__":
    client = Client()

    response = client.GetServiceInfoTaskInfo(
        cpu_cores=4, ram_gb=8, disk_gb=100, preemptible=True, zones=[]
    )
    print(response)
