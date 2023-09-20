from fastapi import FastAPI
from resources import health_check,sign_in,sign_up

app = FastAPI()
app.include_router(health_check.router)
app.include_router(sign_in.router)
app.include_router(sign_up.router)