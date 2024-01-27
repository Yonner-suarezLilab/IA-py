from flask import Flask
from .extensions import api
from flask_cors import CORS
from .routes.router_empleado import Empleados
from.routes.router_empleador import Empleadores
from .routes.router_chat import Chat
from .Utils.db import db
from .config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
api.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


with app.app_context():
  db.create_all()


CORS(app, resources={r"/*": {"origins": "*"}})


api.add_namespace(Empleados, path='')
api.add_namespace(Empleadores, path='')
api.add_namespace(Chat, path="")


