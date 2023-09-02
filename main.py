from fastapi import FastAPI
# from routes.Invoice import invoice
from routes.Movie import movie
from routes.MovieSchedule import movieSchedule
from routes.Service import service
# from routes.ServiceInvoice import serviceInvoice
from routes.Staff import staff
from routes.Ticket import ticket
from routes.User import user
from routes import health_check,invoice
import uvicorn

app = FastAPI()
app.include_router(invoice)
app.include_router(movie)
app.include_router(movieSchedule)
app.include_router(service)
# app.include_router(serviceInvoice)
app.include_router(staff)
app.include_router(ticket)
app.include_router(user)
app.include_router(health_check)
if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info",reload=True)
    server = uvicorn.Server(config)
    server.run()