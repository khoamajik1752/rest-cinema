from db import conn 
from helpers import CustomModel
InvoiceModel= CustomModel(conn.cinema.Invoice)
MovieModel=conn.cinema.Movie
MovieScheduleModel=conn.cinema.MovieSchedule
ServiceModel=conn.cinema.Service
StaffModel=conn.cinema.Staff
TicketModel=conn.cinema.Ticket
UserModel=conn.cinema.User
RoleModel=conn.cinema.Role
