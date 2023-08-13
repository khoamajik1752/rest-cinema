from fastapi import FastAPI
from routes.Invoice import invoice
from routes.Movie import movie
from routes.MovieSchedule import movieSchedule
from routes.Service import service
from routes.ServiceInvoice import serviceInvoice
from routes.Staff import staff
from routes.Ticket import ticket
from routes.User import user
app = FastAPI()
app.include_router(invoice)
app.include_router(movie)
app.include_router(movieSchedule)
app.include_router(service)
app.include_router(serviceInvoice)
app.include_router(staff)
app.include_router(ticket)
app.include_router(user)
