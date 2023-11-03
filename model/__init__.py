from db import conn
from helpers import CustomModel
UserModel= CustomModel(conn.cinema.user)
ApiKeyModel=CustomModel(conn.cinema.api_key)
MovieModel=CustomModel(conn.cinema.movie)
# ApiKeyModel=conn.cinema.api_key


