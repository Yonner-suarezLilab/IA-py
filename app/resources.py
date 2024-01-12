from flask_restx import Resource, Namespace
from flask import jsonify
from .api_models import requestIA
import openai
from app.Utils.DataEmpleados import DataEmpleado
from app.Utils.DataEmpleador import DataEmpleador
from app.agent.agent import create_agent

Employee = Namespace("Employees")
Employer = Namespace("Employer")
Ia = Namespace("IA")
    
@Employee.route("/GetEmployeesData")
class Employees(Resource):
    def get(self):
        return jsonify({"response": DataEmpleado})

@Employer.route("/GetEmployersData")
class Employees(Resource):
    def get(self):
        return jsonify({"response": DataEmpleador})
    
@Ia.route("/GetRecomendationIA")
class AI(Resource):
    def get(self):
        agent = create_agent()
        response = agent.run("Necesito contratar a un gasista")
        return jsonify({"response": response})
    