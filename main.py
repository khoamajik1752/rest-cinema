from fastapi import FastAPI
from resources import health_check,sign_in,sign_up,api_key
import uvicorn

app = FastAPI()
app.include_router(health_check.router)
app.include_router(sign_in.router)
app.include_router(sign_up.router)
app.include_router(api_key.router)
if __name__ =="__main__":
    uvicorn.run("main:app", port=5000, log_level="info",reload=True)