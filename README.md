# TES-cli

Bravado-based client for GA4GH Task Execution Service (TES) API services

# Installation

Clone repository

```bash
git clone https://github.com/elixir-europe/TES-cli.git
```

Traverse to project directory

```bash
cd TES-cli
```

Create and activate virtual environment

```bash
virtualenv -p `which python3` venv
source venv/bin/activate
```

Install required packages

```bash
pip install -r requirements.txt
```

Use Client to send and receive parameters for the \service-info\tasks-info endpoint
   - open the Client.py file
   - modify the main function ( use the client.GetServiceInfoTaskInfo function)
   - ensure the mock-TES is running 
   - run the script 