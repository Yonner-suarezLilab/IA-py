from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
db = os.environ["MYSQL_DB"]
port = os.environ["MYSQL_PORT"]

SQLALCHEMY_DATABASE_URI = f"mysql://{user}:{password}@{host}:{port}/{db}"
