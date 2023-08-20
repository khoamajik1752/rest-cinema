from pymongo import collection


class CustomModel():

    model = collection
    
    def __init__(self,model:collection):
        self.model = model
        
    def aggregate(self,pipeline=[]):
        _res=self.model.aggregate(pipeline)
        return list(_res)
    
    def find(self,query,projection={},options={}):
        _res=self.find(query,projection,options)
        return list(_res)
        
        
    
    