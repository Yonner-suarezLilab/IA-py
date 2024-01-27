from ..models.Intermedios.tbl_aichamba_trabajos_postulaciones import tbl_aichamba_trabajos_postulaciones
from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado
from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos 
from flask_restx import Resource, Namespace
from ..api_models import  nuevo_empleado, nueva_notificacion_empleado , notificar_postulacion
from ..logic.crear_empleado import create_empleado_from_json
from ..logic.crear_notificacion_empleado import create_notificacion_empleado_from_json 
from ..logic.crear_notificar_postulacion import crear_notificar_postulacion_from_json
from flask import jsonify, request, make_response
from sqlalchemy.orm import joinedload
from ..Utils.db import db 

Empleados = Namespace("Empleado")

    
@Empleados.route("/datos_empleados")
class Employees(Resource):
    def get(self):
      try:
        empleados = tbl_aichamba_empleado.query.all()
        employees_json = [employee.to_dict() for employee in empleados]

        return jsonify({"response": employees_json})
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500


@Empleados.route("/datos_empleado")
class Employee(Resource):
    @Empleados.param('empleado_id', description='ID del empleado para filtrar', type=int, required=True)
    def get(self):
      try:
        empleado_id = request.args.get('empleado_id')
      
        empleado = tbl_aichamba_empleado.query.get(empleado_id)
        employees_json = [empleado.to_dict()]

        return jsonify({"response": employees_json})
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
    

@Empleados.route("/datos_publicaciones")
class Datos_Publicaciones(Resource):
    def get(self):
      try:  
        trabajos_query = tbl_aichamba_trabajos.query.all()
        trabajos_respuesta_json = [trabajo.to_dict() for trabajo in trabajos_query]

        return jsonify({"response": trabajos_respuesta_json})
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
    

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


@Empleados.route("/postulaciones_empleado")
class Postulaciones_empleado(Resource):
    @Empleados.param('empleado_id', description='ID del empleado para postulaciones', type=int, required=True)
    def get(self):
      try:
        empleado_id = request.args.get('empleado_id')
       
       # Crear un objeto de sesión
        session = db.session()

        resultados = (
            session.query(tbl_aichamba_empleado, tbl_aichamba_trabajos_postulaciones, tbl_aichamba_trabajos)
            .join(
                tbl_aichamba_trabajos_postulaciones,
                tbl_aichamba_empleado.aich_int_idempleado == tbl_aichamba_trabajos_postulaciones.aich_int_idempleado
            )
            .join(
                tbl_aichamba_trabajos,
                tbl_aichamba_trabajos_postulaciones.aich_int_idtrabajo == tbl_aichamba_trabajos.aich_int_idtrabajos
            )
            .filter(tbl_aichamba_trabajos_postulaciones.aich_bit_activo == 1)
            .all()
        )
        
        data = [
            {
                "idempleado": empleado.aich_int_idempleado,
                "nombre": empleado.aich_vch_nombre,              
                "descripcion": trabajo.aich_vch_descripcion,
                "imagen": trabajo.aich_vch_imagen,
                "latitud": trabajo.aich_vch_latitud,
                "longitud": trabajo.aich_vch_longitud
            }
            for empleado, postulacion, trabajo in resultados
        ]


        # Crear una respuesta JSON
        response = make_response({"data": data}, 200)
        response.headers["Content-Type"] = "application/json"

        # Devolver la respuesta JSON
        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
