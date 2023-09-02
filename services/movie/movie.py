
from models import MovieModel
from schemas.movie import * 

from bson import ObjectId
from helpers.CustomModel import CustomModel

class MovieServices:
    
    model=CustomModel(MovieModel)
    
    @classmethod
    def get_all_movie(cls) -> list[movie_get_response]:
        
        _res=cls.model.find()
        
        return _res
    
    @classmethod
    def get_movie(cls,form_data:movie_get_request) -> list[movie_get_response]:
        # print(type(form_data))
        # data=dict(form_data)
        # print(data)
        query=form_data.dict()
        print({**query})
        _res=cls.model.find({**query})
  
        return _res   
     
    @classmethod
    def create_movie(cls,form_data:movie_create_request) -> movie_create_response:
        
        document=form_data
        _res=cls.model.insert_one(dict(document))
        
        return _res
    
    @classmethod
    def update_movie(cls,form_data:movie_update_request) -> movie_update_response:
        
        filter={"_id":ObjectId(form_data.id)}
        update={'$set':dict(form_data)}
        _res=cls.model.find_one_and_update(filter,update)
        
        return _res
    
    @classmethod
    def delete_movie(cls,form_data:movie_delete_request) -> movie_delete_response:
        
        filter={'_id':ObjectId(form_data.id)}
        _res=cls.model.find_one_and_delete(filter)
        
        
        return _res