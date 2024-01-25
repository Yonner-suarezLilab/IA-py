from flask_restx import Resource, Namespace
from flask import jsonify, request
from ..models.Empleador.tbl_aichamba_empleador import tbl_aichamba_empleador
from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado
from ..Utils.db import db 
from ..api_models import  nuevo_empleado

Empleados = Namespace("Empleado")

    
@Empleados.route("/GetEmployeesData")
class Employees(Resource):
    def get(self):
        empleados = tbl_aichamba_empleado.query.all()
        employees_json = [employee.to_dict() for employee in empleados]
        return jsonify({"response": employees_json})
    
@Empleados.route("/addEmployee")
class AddEmployees(Resource):
    @Empleados.expect(nuevo_empleado)
    def post(self):
        # Obtén los datos del cuerpo de la solicitud utilizando el modelo new_Employee
        data = request.json

        # Accede a los campos del modelo
        name = data.get('Name')
        phone = data.get('Phone')

        new_employee = tbl_aichamba_empleado(nombre=name, Telefono=phone)

        # Agrega y guarda en la base de datos
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({"response": "DataEmpleado"})
    
@Empleados.route("/GetSummaryEmployee")
class EmployeesSumary(Resource):
    def get(self):
        empleados = db.session.query(tbl_aichamba_empleado).all()
        return jsonify({"response":
         empleados})

