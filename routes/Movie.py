from fastapi import APIRouter
from models.Movie import Movie
from db import conn
from helpers import serializeDict, serializeList
from bson import ObjectId
movie = APIRouter(
    prefix="/movie",
    tags=['movie']
)

@movie.get('/')
async def find_all_Movies():
    return serializeList(conn.local.Movie.find())

@movie.get('/{id}')
async def find_one_Movie(id):
    return serializeDict(conn.local.Movie.find_one({"_id":ObjectId(id)}))

@movie.post('/')
async def create_Movie(Movie: Movie):
    conn.local.Movie.insert_one(dict(Movie))
    return serializeDict(conn.local.Movie.find())

@movie.put('/{id}')
async def update_Movie(id,Movie: Movie):
    conn.local.Movie.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Movie)
    })
    return serializeDict(conn.local.Movie.find_one({"_id":ObjectId(id)}))

@movie.delete('/{id}')
async def delete_Movie(id):
    return serializeDict(conn.local.Movie.find_one_and_delete({"_id":ObjectId(id)}))