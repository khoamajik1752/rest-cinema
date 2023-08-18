from fastapi import APIRouter
from schemas import movie_create_request,movie_update_request,movie_get_request,movie_delete_request
from db import conn
from helpers import serializeDict, serializeList
from services.movie.movie import MovieServices
movie = APIRouter(
    prefix="/movie",
    tags=['movie']
)

@movie.get('/')
async def find_all_Movies():
    return serializeList(MovieServices.get_all_movie())

@movie.get('/{name}')
async def find_Movie(name):
    return serializeDict(MovieServices.get_movie(name))

@movie.post('/')
async def create_Movie(Movie: movie_create_request):
    return serializeDict(MovieServices.create_movie(Movie))

@movie.put('/')
async def update_Movie(Movie: movie_update_request):
    return serializeDict(MovieServices.update_movie(Movie))

@movie.delete('/{Movie.id}')
async def delete_Movie(Movie: movie_delete_request):
    return serializeDict(MovieServices.delete_movie(Movie))