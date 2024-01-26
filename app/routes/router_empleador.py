from ..api_models import  nuevo_empleador, nueva_notificacion_empleador, nuevo_trabajo, nueva_postulacion
from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos 
from ..logic.crear_empleador import create_empleador_from_json
from ..logic.crear_notificacion_empleador import create_notificacion_empleador_from_json
from..logic.crear_trabajo import crear_trabajo 
from flask import jsonify, request, make_response
from flask_restx import Resource, Namespace
from ..Utils.db import db

from app.models.Empleador.tbl_aichamba_empleador import tbl_aichamba_empleador


Empleadores = Namespace("Empleador")


@Empleadores.route("/datos_empleadores")
class Datos_Empleadores(Resource):
    def get(self):
        
        empleados_query = tbl_aichamba_empleador.query.all()
        empleados_respuesta_json = [empleado.to_dict() for empleado in empleados_query]

        return jsonify({"response": empleados_respuesta_json})
    
@Empleadores.route("/datos_publicaciones")
class Datos_Publicaciones(Resource):
    def get(self):
        
        trabajos_query = tbl_aichamba_trabajos.query.all()
        trabajos_respuesta_json = [trabajo.to_dict() for trabajo in trabajos_query]

        return jsonify({"response": trabajos_respuesta_json})
    
@Empleadores.route("/empleador")
class Empleador(Resource):
    @Empleadores.expect(nuevo_empleador)  
    def post(self):
        
        data = request.json
        
        empleador_nuevo = create_empleador_from_json(data)
      
        db.session.add(empleador_nuevo)
        db.session.commit()

        response = make_response({"message": "Empleador creado exitosamente"}, 200)

        return response

@Empleadores.route("/notificacion_empleador")
class Notificacion(Resource):
    @Empleadores.expect(nueva_notificacion_empleador)
    def post(self):
        
        data = request.json

        nueva_notificacion = create_notificacion_empleador_from_json(data)

        # Agrega y guarda en la base de datos
        db.session.add(nueva_notificacion)
        db.session.commit()

        response = make_response({"message": "Notificación creada exitosamente"}, 200)
        
        return response


@Empleadores.route("/trabajo")
class Trabajos(Resource):
    @Empleadores.expect(nuevo_trabajo)
    def post(self):
        
        data = request.json

        trabajo_nuevo = crear_trabajo(data)

        # Agrega y guarda en la base de datos
        db.session.add(trabajo_nuevo)
        db.session.commit()

        response = make_response({"message": "Trabajo creado exitosamente"}, 200)
        
        return response
    
@Empleadores.route("/postulacion")
class Trabajos(Resource):
    @Empleadores.expect(nueva_postulacion)
    def post(self):
        
        data = request.json

        postulacion_nueva = crear_trabajo(data)

        # Agrega y guarda en la base de datos
        db.session.add(postulacion_nueva)
        db.session.commit()

        response = make_response({"message": "Postulacion creada exitosamente"}, 200)
        
        return response