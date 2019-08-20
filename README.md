# TES-cli

This repository contains a [Bravado]-based client for a [modified] version of
the [Task Execution Service] API schema of the [Global Alliance for Genomics and
Health], as described in the [mock-TES] repository. The client was developed for
the use within the [TEStribute] task distribution logic application.

## Usage

To use the client import it as follows in your Python code after
[installation](#Installation):

```py
from tes_client import Client

client = Client.Client("http://localhost:9001/ga4gh/tes/v1/")
```

> Note that the indicated URL is valid when [mock-TES] was installed at the
> default location on your local machine. When a different TES instance is
> supposed to be used, replace the full URL (including `http://` or `https://`.

Access the [mock-TES] `/tasks/task-info` endpoint with, e.g.:

```py
response = client.GetTaskInfo(
    cpu_cores=4,
    ram_gb=8,
    disk_gb=100,
    preemptible=True,
    zones=[],
    execution_time_min=10,
)
```

Access the [mock-TES] `/update-config` endpoint with, e.g.:

```py
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
```

Note that the original TES endpoints are currently not implemented.

## Installation

You can install `TES-cli` in one of two ways:

### Manual installation

```bash
git clone https://github.com/elixir-europe/TES-cli.git
python TES-cli/setup.py install
```

### Installation via package manager

```bash
pip install -e git+https://github.com/elixir-europe/TES-cli.git#egg=tes_client
```

## Contributing

This project is a community effort and lives off your contributions, be it in
the form of bug reports, feature requests, discussions, or fixes and other code
changes. Please read the [contributing guidelines] if you want to contribute.
And please mind the [code of conduct] for all interactions with the community.

## Versioning

Development of the app is currently still in alpha stage, and current versioning
is for internal use only. In the future, we are aiming to adopt [semantic
versioning] that is synchronized to the versioning of [TEStribute] and
[mock-TES] in order to ensure that these apps will be compatible as long as both
their major and minor versions match.

## License

This project is covered by the [Apache License 2.0] also available [shippied
with this repository](LICENSE).

## Contact

Please contact the [project leader](mailto:alexander.kanitz@sib.swiss) for
inquiries, proposals, questions etc. that are not covered by the
[Contributing](#Contributing) section.

## Acknowledgments

The project is a collaborative effort under the umbrella of the [ELIXIR Cloud
and AAI] group. It was started during the [2019 Google Summer of Code] as part
of the [Global Alliance for Genomics and Health] [organization].

![logo banner]

[2019 Google Summer of Code]: <https://summerofcode.withgoogle.com/projects/#6613336345542656>
[Bravado]: <https://github.com/Yelp/bravado>
[ELIXIR Cloud and AAI]: <https://elixir-europe.github.io/cloud/>
[Global Alliance for Genomics and Health]: <https://www.ga4gh.org/>
[logo banner]: logos/logo-banner.svg
[mock-TES]: <https://github.com/elixir-europe/mock-TES>
[modified]: <https://github.com/elixir-europe/mock-TES/blob/master/mock_tes/specs/schema.task_execution_service.d55bf88.openapi.modified.yaml>
[Open API specification]: <https://github.com/elixir-europe/mock-TES/blob/master/mock_tes/specs/schema.task_execution_service.d55bf88.openapi.modified.yaml>
[organization]: <https://summerofcode.withgoogle.com/organizations/6643588285333504/>
[Task Execution Service]: <https://github.com/ga4gh/task-execution-schemas>
[TEStribute]: <https://github.com/elixir-europe/TEStribute>
