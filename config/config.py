# config/config.py
from decouple import config

# Database configuration
USER = config("USER")
HOST = config("HOST")
PORT = config("PORT")
PASSWORD = config("PASSWORD")
DATABASE = config("DATABASE")
