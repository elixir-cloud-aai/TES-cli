# TES-cli

[![Apache License](https://img.shields.io/badge/license-Apache%202.0-orange.svg?style=flat&color=important)](http://www.apache.org/licenses/LICENSE-2.0)
![GitHub: latest tag](https://flat.badgen.net/github/tag/elixir-europe/TES-cli?color=cyan&icon=github)
[![PyPI](https://img.shields.io/pypi/pyversions/tes-client.svg?style=flat)](https://pypi.python.org/pypi/tes-client)
[![PyPI](https://img.shields.io/pypi/v/tes_client.svg?style=flat&color=bright-green)](https://pypi.python.org/pypi/tes_client)

This repository contains a [Bravado]-based client for a [modified] version of
the [Task Execution Service] API schema of the [Global Alliance for Genomics and
Health], as described in the [mock-TES] repository. The client was developed for
the use within the [TEStribute] task distribution logic application.

## Usage

To use the client import it as follows in your Python code after
[installation](#Installation):

```py
import tes_client

client = tes_client.Client("http://localhost:9001/ga4gh/tes/v1/")
```

It is possible to supply a Bearer token, which will then be added to the
`Authentication` header (prepended by `Bearer`) for every outbound call:

```py
client = tes_client.Client(
   url="https://path.to/swagger.json",
   jwt="SomET0kEn"
)
```

> Note that the indicated URL is valid when [mock-TES] was installed at the
> default location on your local machine. When a different TES instance is
> supposed to be used, replace the full URL (including `http://` or `https://`).

Access the [mock-TES] `POST /tasks/task-info` endpoint with, e.g.:

```py
response = client.getTaskInfo(
    cpu_cores=4,
    ram_gb=8,
    disk_gb=100,
    execution_time_min=10,
)
```

Access the [mock-TES] `POST /update-config` endpoint with, e.g.:

```py
response = client.updateTaskInfoConfig(
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
cd TES-cli
python setup.py install
```

### Installation via package manager

```bash
pip install drs_client
```

or (for development version)

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

This project is covered by the [Apache License 2.0] also available [shipped
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

[Apache License 2.0]: <https://www.apache.org/licenses/LICENSE-2.0>
[2019 Google Summer of Code]: <https://summerofcode.withgoogle.com/projects/#6613336345542656>
[Bravado]: <https://github.com/Yelp/bravado>
[contributing guidelines]: CONTRIBUTING.md
[code of conduct]: CODE_OF_CONDUCT.md
[ELIXIR Cloud and AAI]: <https://elixir-europe.github.io/cloud/>
[Global Alliance for Genomics and Health]: <https://www.ga4gh.org/>
[logo banner]: logos/logo-banner.svg
[mock-TES]: <https://github.com/elixir-europe/mock-TES>
[modified]: <https://github.com/elixir-europe/mock-TES/blob/master/mock_tes/specs/schema.task_execution_service.d55bf88.openapi.modified.yaml>
[organization]: <https://summerofcode.withgoogle.com/organizations/6643588285333504/>
[semantic versioning]: <https://semver.org/>
[Task Execution Service]: <https://github.com/ga4gh/task-execution-schemas>
[TEStribute]: <https://github.com/elixir-europe/TEStribute>
