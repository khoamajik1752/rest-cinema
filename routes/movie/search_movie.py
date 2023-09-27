from .movie import router
from schemas import SearchMovieSchema
from fastapi import Depends

@router.get('/search')
def get_movie(query_params:SearchMovieSchema=Depends()):

    #TODO: implements search movie logic
    return {}