from flask import Flask
from .extensions import api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .routes.resources import Employee, Employer
from .Utils.db import db
import config

app = Flask(__name__)
api.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:judasaki@localhost:3308/iachamba"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


with app.app_context():
  db.create_all()
#SQLAlchemy(app)


CORS(app, resources={r"/*": {"origins": "*"}})


api.add_namespace(Employee, path='/employees')
api.add_namespace(Employer, path='/employers')


