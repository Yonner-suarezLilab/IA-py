from ..api_models import  nuevo_empleador, nueva_notificacion_empleador, nuevo_trabajo, nueva_postulacion, nuevo_chat
from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos 
from ..models.Intermedios.tbl_aichamba_trabajos_postulaciones import tbl_aichamba_trabajos_postulaciones
from ..logic.crear_empleador import create_empleador_from_json
from ..logic.crear_notificacion_empleador import create_notificacion_empleador_from_json
from..logic.crear_trabajo import crear_trabajo 
from ..logic.crear_postulacion import crear_postulacion
from flask import jsonify, request, make_response
from flask_restx import Resource, Namespace
from ..Utils.db import db
from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos 
from app.models.Empleador.tbl_aichamba_empleador import tbl_aichamba_empleador
from app.models.Empleador.tbl_aichamba_notificacion_empleador import tbl_aichamba_notificacion_empleador


Empleadores = Namespace("Empleador")


@Empleadores.route("/datos_empleador")
class Datos_empleador(Resource):
    @Empleadores.param('empleador_id', description='ID del empleador para filtrar', type=int, required=True)
    def get(self):
      try:
        empleador_id = request.args.get('empleador_id')
      
        empleador = tbl_aichamba_empleador.query.get(empleador_id)
        empleadores_json = [empleador.to_dict()]

        return jsonify({"response": empleadores_json})
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500

@Empleadores.route("/datos_empleadores")
class Datos_Empleadores(Resource):
    def get(self):
      try:
        empleados_query = tbl_aichamba_empleador.query.all()
        empleados_respuesta_json = [empleado.to_dict() for empleado in empleados_query]

        return jsonify({"response": empleados_respuesta_json})
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
    
@Empleadores.route("/empleador")
class Empleador(Resource):
    @Empleadores.expect(nuevo_empleador)  
    def post(self):
      try:
        data = request.json
        
        empleador_nuevo = create_empleador_from_json(data)
      
        db.session.add(empleador_nuevo)
        db.session.commit()

        response = make_response({"message": "Empleador creado exitosamente"}, 200)

        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
      


@Empleadores.route("/notificacion_empleador")
class Notificacion(Resource):
    @Empleadores.expect(nueva_notificacion_empleador)
    def post(self):
      try:
        data = request.json

        nueva_notificacion = create_notificacion_empleador_from_json(data)

        # Agrega y guarda en la base de datos
        db.session.add(nueva_notificacion)
        db.session.commit()

        response = make_response({"message": "Notificación creada exitosamente"}, 200)
        
        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500

@Empleadores.route("/trabajo")
class Trabajos(Resource):
    @Empleadores.expect(nuevo_trabajo)
    def post(self):
      try:
        data = request.json

        empleado_id = data.get("idEmpleador")

        empleador = tbl_aichamba_empleador.query.get(empleado_id)

        # Verificar si el objeto empleado y sus atributos existen
        if empleador and hasattr(empleador, 'aich_vch_longitud') and hasattr(empleador, 'aich_vch_latitud'):
            # Obtener los valores de longitud y latitud
            longitud = empleador.aich_vch_longitud
            latitud = empleador.aich_vch_latitud

            # Luego puedes usar estos valores al crear el trabajo
            trabajo_nuevo = crear_trabajo(data=data, latitud=latitud, longitud=longitud)
             # Agrega y guarda en la base de datos
            db.session.add(trabajo_nuevo)
            db.session.commit()

            response = make_response({"message": "Trabajo creado exitosamente"}, 200)
        else:       
            make_response({"message": "Error: No se pudo obtener la longitud y latitud del empleado."}, 400)   
        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
      

@Empleadores.route("/postulacion")
class Postulacion(Resource):
    @Empleadores.expect(nueva_postulacion)
    def post(self):
      try:
        data = request.json

        postulacion_nueva = crear_postulacion(data)

        # Agrega y guarda en la base de datos
        db.session.add(postulacion_nueva)
        db.session.commit()

        response = make_response({"message": "Postulacion creada exitosamente"}, 200)
        
        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
      

      
@Empleadores.route("/postulantes_publicaciones")    
class PostulantesPublicaciones(Resource):
        @Empleadores.param('id_trabajo', description='ID de trabajo para filtrar postulantes', type=int, required=True)
        def get(self):
          try:
            # Obtén el valor del parámetro aich_int_idtrabajo desde request.args
            id_trabajo = request.args.get('id_trabajo', type=int)

            # Verifica si se proporciona el parámetro
            if id_trabajo is not None:
                postulantes_query = tbl_aichamba_trabajos_postulaciones.query.filter_by(aich_int_idtrabajo=id_trabajo).all()

                # Convierte los resultados a formato JSON
                postulantes_respuesta_json = [postulante.to_dict() for postulante in postulantes_query]
                
                # Devuelve la respuesta en formato JSON
                return jsonify({"response": postulantes_respuesta_json})
            else:
                # Si no se proporciona el parámetro, devuelve un error 400 (Bad Request) con un mensaje
                return jsonify({"error": "Debe especificar el IdTrabajo para ver los postulantes a la publicación"}), 400
          except Exception as e:
            error_message = {"error": str(e)}
            print(e)
            return error_message, 500


@Empleadores.route("/publicaciones_por_empleador")    
class PublicacionesEmpleador(Resource):
    @Empleadores.param('id_empleador', description='ID del empleador para filtrar publicaciones', type=int, required=True)
    def get(self):
      try:
        # Obtén el valor del parámetro id_empleador desde request.args
        idempleador = request.args.get('id_empleador', type=int)

        # Verifica si se proporciona el parámetro
        if idempleador is not None:
            publicaciones_query = tbl_aichamba_trabajos.query.filter_by(aich_int_idempleador=idempleador).all()

            # Convierte los resultados a formato JSON
            publicaciones_respuesta_json = [publicaciones.to_dict() for publicaciones in publicaciones_query]
            
            # Devuelve la respuesta en formato JSON
            return jsonify({"response": publicaciones_respuesta_json})
        else:
            # Si no se proporciona el parámetro, devuelve un error 400 (Bad Request) con un mensaje
            return jsonify({"error": "Debe especificar el Id_empleador para ver sus publicaciones"}), 400
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500


@Empleadores.route("/notificaciones_empleador")    
class NotificacionesEmpleador(Resource):
    @Empleadores.param('id_empleador', description='ID del empleador para filtrar notificaciones', type=int, required=True)
    def get(self):
      try:
        # Obtén el valor del parámetro id_empleador desde request.args
        idempleador = request.args.get('id_empleador', type=int)

        # Verifica si se proporciona el parámetro
        if idempleador is not None:
            notificaciones_query = tbl_aichamba_notificacion_empleador.query.filter_by(aich_vch_idempleador=idempleador).all()

            # Convierte los resultados a formato JSON
            notificaciones_respuesta_json = [notificaciones.to_dict() for notificaciones in notificaciones_query]    
            
            # Devuelve la respuesta en formato JSON
            return jsonify({"response": notificaciones_respuesta_json})
        else:
            # Si no se proporciona el parámetro, devuelve un error 400 (Bad Request) con un mensaje
            return jsonify({"error": "Debe especificar el Id_empleador para ver sus notificaciones"}), 400
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
      
