
from models import MovieModel
from schemas import  movie_create_request, movie_create_response, movie_get_request, movie_get_response, movie_update_request, movie_update_response ,movie_delete_request, movie_delete_response

from bson import ObjectId
from pymongo import ReturnDocument

class MovieServices:
    @classmethod
    def get_all_movie(cls) -> list[movie_get_response]:
        _movie=MovieModel.find()
        if _movie is None:
            raise Exception('Khong thay phim')
        
        return _movie
    
    @classmethod
    def get_movie(cls,form_data:str) -> movie_get_response:
        name=form_data

        _movie=MovieModel.find({"Name":name})
        if _movie is None:
            raise Exception('Khong thay phim')    
        
        return _movie   
     
    @classmethod
    def create_movie(cls,form_data:movie_create_request) -> movie_create_response:
        name=form_data.Name
        author=form_data.Author
        description=form_data.Description

        movieid=MovieModel.insert_one({"Name":name,"Author":author,"Description":description})
        if movieid is None:
            raise Exception('Khong tao duoc phim')
        
        _res=MovieModel.find_one({"_id":ObjectId(movieid.inserted_id)})
        
        return _res
    
    @classmethod
    def update_movie(cls,form_data:movie_update_request) -> movie_update_response:
        id=form_data.id
        name=form_data.Name
        author=form_data.Author
        description=form_data.Description
        _res=MovieModel.find_one_and_update({"_id":ObjectId(id)},{
            "$set":{
                "Name":name,
                "Author": author,
                "Description":description
            }
        })
        
        return _res
    
    @classmethod
    def delete_movie(cls,form_data:movie_delete_request) -> movie_delete_response:
        id=form_data.id
        _res=MovieModel.find_one_and_delete({"_id":ObjectId(id)})
        
        
        return _res