from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado
from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos 
from flask_restx import Resource, Namespace
from ..api_models import  nuevo_empleado, nueva_notificacion_empleado , notificar_postulacion
from ..logic.crear_empleado import create_empleado_from_json
from ..logic.crear_notificacion_empleado import create_notificacion_empleado_from_json 
from ..logic.crear_notificar_postulacion import crear_notificar_postulacion_from_json
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
    @Empleados.param('empleado_id', description='ID del empleado para filtrar', type=int, required=True)
    def get(self):
        empleado_id = request.args.get('empleado_id')
        print(empleado_id)
        empleado = tbl_aichamba_empleado.query.get(empleado_id)
        employees_json = [empleado.to_dict()]

        return jsonify({"response": employees_json})
    

@Empleados.route("/datos_publicaciones")
class Datos_Publicaciones(Resource):
    def get(self):
        
        trabajos_query = tbl_aichamba_trabajos.query.all()
        trabajos_respuesta_json = [trabajo.to_dict() for trabajo in trabajos_query]

        return jsonify({"response": trabajos_respuesta_json})
    

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


@Empleados.route("/notificar_postulacion")
class Notificar_postulacion(Resource):
    @Empleados.expect(notificar_postulacion)
    def post(self):
      try:
        data = request.json
       

        notificar_postulacion = crear_notificar_postulacion_from_json(data)

        # Agrega y guarda en la base de datos
        db.session.add(notificar_postulacion)
        db.session.commit()

        response = make_response({"message": "Notificación creada exitosamente"}, 200)
        
        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500


