from fastapi import APIRouter


health_check=APIRouter(
    prefix='/health_check',
    tags=['health_check']
)

@health_check.get('/')
async def healthCheck():
    return 'status: OK'
