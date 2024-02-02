from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
db = os.environ["MYSQL_DB"]
port = os.environ["MYSQL_PORT"]


api_key_ia = os.environ["OPEN_AI_API_KEY"]
default_model = os.environ["DEFAULT_MODEL"]

SQLALCHEMY_DATABASE_URI = f"mysql://{user}:{password}@{host}:{port}/{db}"
