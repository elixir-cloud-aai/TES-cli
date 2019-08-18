# TES-cli

This repository contains a [bravado]-based client for modified GA4GH Data Repository Service (DRS) API services the 
[Open API specification] for which can be found in the [mock-TES] repository along with a mock-service for the same.

# Installation

Install as a package on your chosen python environment.

Clone repository
```bash
git clone https://github.com/elixir-europe/TES-cli.git
```

Traverse project repository 
```bash
cd TES-cli
python setup.py install
```

To use the client import to the python script as follows
```python
from tes_client import Client
client = Client.Client("the-tes-uri")
```

**_or_**

Use the ```gihub -e git+https://github.com/elixir-europe/DRS-cli.git#egg=TES_cli``` to this repository and add it to your 
requirements 

To test the working of the client you can run the main of the [client](tes_client/Client.py) script which currently 
returns a response from one of the live mock services.

[TESTribute]:https://github.com/elixir-europe/TEStribute 
[mock-TES]:https://github.com/elixir-europe/mock-TES
[bravado]:https://github.com/Yelp/bravado
[Open API specification]:https://github.com/elixir-europe/mock-TES/blob/master/mock_tes/specs/schema.task_execution_service.d55bf88.openapi.modified.yaml
