from fastapi import APIRouter
from models.MovieSchedule import MovieSchedule
from db import conn
from helpers import serializeDict, serializeList
from bson import ObjectId
movieSchedule = APIRouter(
    prefix="/movieSchedule",
    tags=['movieSchedule']
)

@movieSchedule.get('/')
async def find_all_MovieSchedules():
    return serializeList(conn.local.MovieSchedule.find())

@movieSchedule.get('/{id}')
async def find_one_MovieSchedule(id):
    return serializeDict(conn.local.MovieSchedule.find_one({"_id":ObjectId(id)}))

@movieSchedule.post('/')
async def create_MovieSchedule(MovieSchedule: MovieSchedule):
    if conn.local.Movie.find_one({"_id":ObjectId(MovieSchedule.MovieId)}):
        conn.local.MovieSchedule.insert_one(dict(MovieSchedule))
    return serializeDict(conn.local.MovieSchedule.find())

@movieSchedule.put('/{id}')
async def update_MovieSchedule(id,MovieSchedule: MovieSchedule):
    if conn.local.Movie.find_one({"_id":ObjectId(MovieSchedule.MovieId)}):
        conn.local.MovieSchedule.find_one_and_update({"_id":ObjectId(id)},{
           "$set":dict(MovieSchedule)
        })
    return serializeDict(conn.local.MovieSchedule.find_one({"_id":ObjectId(id)}))

@movieSchedule.delete('/{id}')
async def delete_MovieSchedule(id):
    return serializeDict(conn.local.MovieSchedule.find_one_and_delete({"_id":ObjectId(id)}))