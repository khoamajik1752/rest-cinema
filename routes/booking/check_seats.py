from .booking import router
from schemas import *

@router.get('/check_availabity')
def check_availability():
    
    return {}