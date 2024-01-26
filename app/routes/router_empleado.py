from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado
from flask_restx import Resource, Namespace
from ..api_models import  nuevo_empleado, nueva_notificacion_empleado
from ..logic.crear_empleado import create_empleado_from_json
from ..logic.crear_notificacion_empleado import create_notificacion_empleado_from_json
from flask import jsonify, request, make_response
from ..Utils.db import db 

Empleados = Namespace("Empleado")

    
@Empleados.route("/datos_empleados")
class Employees(Resource):
    def get(self):
        empleados = tbl_aichamba_empleado.query.all()
        employees_json = [employee.to_dict() for employee in empleados]

        return jsonify({"response": employees_json})

@Empleados.route("/datos_empleado")
class Employee(Resource):
    def get(self, empleado_id):
        empleado_id = request.args.get('empleado_id')
        print(empleado_id)
        empleados = tbl_aichamba_empleado.query.get(empleado_id)
        employees_json = [employee.to_dict() for employee in empleados]

        return jsonify({"response": employees_json})
    
@Empleados.route("/empleado")
class AddEmployee(Resource):
    @Empleados.expect(nuevo_empleado)
    def post(self):

      try:  
        data = request.json

        empleado_nuevo = create_empleado_from_json(data)

        # Agrega y guarda en la base de datos
        db.session.add(empleado_nuevo)
        db.session.commit()

        response = make_response({"message": "Empleado creado exitosamente"}, 200)

        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
    
@Empleados.route("/notificacion_empleado")
class EmployeesSumary(Resource):
    @Empleados.expect(nueva_notificacion_empleado)
    def post(self):
      try:
        data = request.json
       

        nueva_notificacion = create_notificacion_empleado_from_json(data)

        # Agrega y guarda en la base de datos
        db.session.add(nueva_notificacion)
        db.session.commit()

        response = make_response({"message": "Notificación creada exitosamente"}, 200)
        
        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500

