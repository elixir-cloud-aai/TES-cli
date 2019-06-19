"""
Client script for the mock Task Execution Service
"""

from bravado.client import SwaggerClient, CallableOperation
from bravado_core.formatter import DEFAULT_FORMATS


#connexion stub runs on port 5000 and the schema is available at this endpoint
connexion_url = 'http://127.0.0.1:5000/ga4gh/tes/v1'

#specify config for bravado
DEFAULT_CONFIG = {'validate_requests':False,
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
    
    #function to generate a TesTask that can be posted
    def DefineTask(self,id):
        tesTask = self.models.get_model('tesTask')
        tesExecutor = self.models.get_model('tesExecutor')
        #to-implement
        return tesTask(executors=[tesExecutor(image='',command=[]),tesExecutor(image='',command=[])])  
                  
    def ListTasks(self,name_prefix,page_size,page_token,view='BASIC'):
        return self.client.ListTasks(view=view,name_prefix=name_prefix,page_size=page_size,page_token=page_token).result()

    def GetServiceInfo(self):
        return self.client.GetServiceInfo().result()
    
    def GetServiceInfoTaskInfo(self):
        return self.client.GetServiceInfoTaskInfo().result()
    
    def GetTask(self,task_id):
        return self.client.GetTask(id=task_id).result()
    
    def CreateTask(self,tesTask):
        return self.client.CreateTask(body=tesTask).result()
    
    def  CancelTask(self,task_id):
        return self.client.CancelTask(id=task_id).result()
        
if __name__ == '__main__':
    client = Client()
    
    #to-fix: DefineTask funtion
    #client.CreateTask(client.DefineTask("id"))
            
            