from tes_client import Client

client = Client.Client("http://localhost:9001/ga4gh/tes/v1")

response = client.GetTaskInfo(
    cpu_cores=4,
    ram_gb=8,
    disk_gb=100,
    preemptible=True,
    zones=[],
    execution_time_min=10,
)
print(response)

response = client.UpdateTaskInfoConfig(
    currency="USD",
    time_unit="MINUTES",
    unit_costs={
        "cpu_usage": 1,
        "memory_consumption": 4,
        "data_storage": 10,
        "data_transfer": 20,
    },
)
print(response)
