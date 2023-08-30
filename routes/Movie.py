from fastapi import APIRouter,Depends
from schemas.movie import *
from db import conn
from helpers import serializeDict, serializeList
from services.movie.movie import MovieServices
movie = APIRouter(
    prefix="/movie",
    tags=['movie']
)

@movie.get('/')
async def find_all_Movies()->list[movie_get_response]:
    return MovieServices.get_all_movie()

@movie.get('/{Movie.Name}')
async def find_Movie(Movie: movie_get_request=Depends())->list[movie_get_response]:
    return MovieServices.get_movie(Movie)

@movie.post('/')
async def create_Movie(Movie: movie_create_request)->movie_create_response:
    return MovieServices.create_movie(Movie)

@movie.put('/')
async def update_Movie(Movie: movie_update_request)->movie_update_response:
    return MovieServices.update_movie(Movie)

@movie.delete('/{Movie.id}')
async def delete_Movie(Movie: movie_delete_request)->movie_delete_response:
    return MovieServices.delete_movie(Movie)