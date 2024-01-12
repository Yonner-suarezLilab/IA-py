from flask import Flask
from .extensions import api
from .resources import Employee, Employer, Ia

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    api.add_namespace(Employee, path='/employees')
    api.add_namespace(Employer, path='/employers')
    api.add_namespace(Ia, path='/ia')
    return app

