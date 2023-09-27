from fastapi import FastAPI
# from routes.Invoice import invoice

from routes import HeathCheck, movie
import uvicorn

app = FastAPI()

app.include_router(HeathCheck.router)
app.include_router(movie.router)


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info",reload=True)
    server = uvicorn.Server(config)
    server.run()