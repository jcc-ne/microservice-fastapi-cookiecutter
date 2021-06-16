from os import environ, path
from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, ".env"))

# Database config
DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_USER = environ.get("DATABASE_USER")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
DATABASE_PORT = environ.get("DATABASE_PORT")
DATABASE_NAME = environ.get("DATABASE_NAME")

REDIS_HOST = environ.get("REDIS_HOST")
REDIS_PORT = environ.get("REDIS_PORT")

LOG_LEVEL = environ.get("LOG_LEVEL", 30)
