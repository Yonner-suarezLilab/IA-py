from flask_restx import Resource, Namespace
from flask import jsonify
from .api_models import requestIA
import openai
from app.Utils.DataEmpleados import DataEmpleado
from app.Utils.DataEmpleador import DataEmpleador

Employee = Namespace("Employees")
Employer = Namespace("Employer")
    
@Employee.route("/GetEmployeesData")
class Employees(Resource):
    def get(self):
        return jsonify({"response": DataEmpleado})

@Employer.route("/GetEmployersData")
class Employees(Resource):
    def get(self):
        return jsonify({"response": DataEmpleador})
    
