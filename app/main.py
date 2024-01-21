from flask import Flask
# from flask import MySQL
from .extensions import api
from .resources import Employee, Employer
import openai
from flask_cors import CORS

# secret key open ia

openai.api_key="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"

def create_app():
    app = Flask(__name__)
    app.Config["MYSQL_HOST"] = "localhost"
    app.Config["MYSQL_USER"] = "root"
    app.Config["MYSQL_PASSWORD"] = "judasaki"
    app.Config["MYSQL_DB"] = "iachamba"
    # mysql = MySQL(app)
    api.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    api.add_namespace(Employee, path='/employees')

    api.add_namespace(Employer, path='/employers')
    return app





