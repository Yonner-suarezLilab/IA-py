from flask_restx import Resource, Namespace
from flask import jsonify
from .api_models import requestIA
import openai
from app.Utils.DataEmpleados import DataEmpleado
from app.Utils.DataEmpleador import DataEmpleador
from app.Utils.ResumenEmpleado import ResumenEmpleado
from app.Utils.PropuestaEmpleadores import PropuestaEmpleador
from app.Utils.notificationsEmployee import notificationsEmployee

Employee = Namespace("Employees")
Employer = Namespace("Employer")

@Employee.route("/GetEmployeesData")
class Employees(Resource):
    def get(self):
        return jsonify({"response": DataEmpleado})

@Employee.route("/GetSummaryEmployee")
class Employees(Resource):
    def get(self):
        return jsonify({"response": ResumenEmpleado})

@Employer.route("/GetEmployersData")
class Employees(Resource):
    def get(self):
        return jsonify({"response": DataEmpleador})

@Employer.route("/GetProposalEmployer")
class Employees(Resource):
    def get(self):
        return jsonify({"response": PropuestaEmpleador})

@Employer.route("/GetNotificationsEmployee")
class Employees(Resource):
    def get(self):
        return jsonify({"response": notificationsEmployee})
