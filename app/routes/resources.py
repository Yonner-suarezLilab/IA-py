from flask_restx import Resource, Namespace
from flask import jsonify, request
from app.Utils.DataEmpleados import DataEmpleado
from app.Utils.DataEmpleador import DataEmpleador
from app.Utils.ResumenEmpleado import ResumenEmpleado
from app.Utils.PropuestaEmpleadores import PropuestaEmpleador
from ..models.EmployerDB import EmployerDB
from ..Utils.db import db 
from ..api_models import new_Employee

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
    
@Employer.route("/PostProposalEmployer")
class Employees(Resource):
    @Employer.expect(new_Employee)  # Especifica que espera un modelo new_Employee
    def post(self):
        # Obtén los datos del cuerpo de la solicitud utilizando el modelo new_Employee
        data = request.json

        # Accede a los campos del modelo
        name = data.get('Name')
        email = data.get('Email')
        
        # Crea una nueva instancia de EmployerDB
        new_employee = EmployerDB(nombre=name, email=email)

        # Agrega y guarda en la base de datos
        db.session.add(new_employee)
        db.session.commit()

        return jsonify({"response": "PropuestaEmpleador"})
