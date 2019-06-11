"""
Client script for the mock Task Execution Service
"""

from bravado.client import SwaggerClient, CallableOperation
from bravado_core.formatter import DEFAULT_FORMATS


#connexion stub runs on port 5000 and the schema is available at this endpoint
connexion_url = 'http://127.0.0.1:5000/ga4gh/tes/v1'

#specify config for bravado
DEFAULT_CONFIG = {'validate_responses':True,
                  'headers':None,
                  'formats':DEFAULT_FORMATS['int64']}

#define a clinet
class Client:
    def __init__(self, url=connexion_url, config=DEFAULT_CONFIG):
        self._config = config
        config['formats'] = [DEFAULT_FORMATS['int64']]
        swagger_path = '{}/swagger.json'.format(url.rstrip('/'))
        
        self.models = SwaggerClient.from_url(swagger_path, config=config)
        self.client = self.models.TaskService
            

#a few tasks using the sevice 
def main():
    client = Client()
    c = client.client
    
    print("The available services are : ",dir(c))
    
    # CreateTaskObject
    tesTask = client.models.get_model('tesTask')
    tesExecutor = client.models.get_model('tesExecutor')

    create_task = tesTask(
            id="001",
            state="QUEUED",
            name="test_task",
            desription="sample task object",
            executor=[{}]
            ) 
    updateTask = c.CreateTask(body=create_task).response()

    #post tasks
    
    #retreive info
    
    
if __name__ == '__main__' :
    main()
    