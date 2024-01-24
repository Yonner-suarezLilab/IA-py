from flask_restx import Resource, Namespace
from flask import jsonify, request
from app.Utils.DataEmpleados import DataEmpleado
from app.Utils.DataEmpleador import DataEmpleador
from app.Utils.ResumenEmpleado import ResumenEmpleado
from app.Utils.PropuestaEmpleadores import PropuestaEmpleador
from ..models.tbl_aichamba_empleador import tbl_aichamba_empleador
from ..models.tbl_aichamba_empleado import tbl_iachamba_empleado
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
        new_employeer = tbl_aichamba_empleador(nombre=name, email=email)
        new_employeer = tbl_iachamba_empleado()

        # Agrega y guarda en la base de datos
        db.session.add(new_employeer)
        db.session.commit()

        return jsonify({"response": "PropuestaEmpleador"})
