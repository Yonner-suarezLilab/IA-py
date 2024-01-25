from ..logic.crear_empleador import create_empleador_from_json
from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos 
from flask_restx import Resource, Namespace, reqparse
from ..api_models import  nuevo_empleador
from flask import jsonify, request, make_response
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
    
@Empleadores.route("/PostProposalEmployer")
class Employees(Resource):
    @Empleadores.expect(nuevo_empleador)  
    def post(self):
        
        data = request.json
        
        empleador_nuevo = create_empleador_from_json(data)
      
        db.session.add(empleador_nuevo)
        db.session.commit()

        response = make_response({"message": "Empleador creado exitosamente"}, 200)

        return response
