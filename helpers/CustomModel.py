from pymongo import collection
from fastapi import HTTPException
from bson import ObjectId


class CustomModel():

    model = collection
    
    def __init__(self,model:collection):
        self.model = model
        
    def aggregate(self,pipeline=[]):
        _res=list(self.model.aggregate(pipeline))
        
        if _res == []:
            raise HTTPException(status_code=404, detail="error not found")
         
        return _res
    
    def find(self,query,projection={},options={}):
        _res=list(self.model.find(query,projection,options))
                
        if _res == []:
            raise HTTPException(status_code=404, detail="error not found")
        
        
        return _res
    
    def find_one(self,query,projection={},options={}):
        _res=self.model.find_one(query,projection,options)
        
        if _res is None:
            raise HTTPException(status_code=404, detail="error not found")
        
        
        return _res
    
    def insert_one(self,document,writeConcern={}):
        _res=self.model.insert_one(document,writeConcern)
        
        return self.model.find_one({'_id':ObjectId(_res.inserted_id)})
    
    def find_one_and_update(self,filter,update):
        _res=self.model.find_one_and_update(filter,update)
        
        if _res is None:
            raise HTTPException(status_code=404, detail="error not found")
        
        return _res
    
    def find_one_and_delete(self,filter):
        _res=self.model.find_one_and_delete(filter)
        
        if _res is None:
            raise HTTPException(status_code=404, detail="error not found")
        
        return _res
        
        
        
        
    
    