from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado
from ..models.Empleador.tbl_aichamba_empleador import tbl_aichamba_empleador
from ..models.Chats.tbl_aichamba_chat import tbl_aichamba_chat
from flask import jsonify, request, make_response , json
from ..api_models import nuevo_chat
from flask_restx import Resource, Namespace
from ..Utils.db import db
from ..logic.crear_chat import crear_chat


Chat = Namespace("Chats")

@Chat.route("/chat_con_empleado")
class Chat_con_empleado(Resource):
    @Chat.expect(nuevo_chat)
    def post(self):
      try:
        data = request.json

        nuevo_chat = crear_chat(data)
        # Agrega y guarda en la base de datos
        db.session.add(nuevo_chat)

        db.session.commit()

        response = make_response({"message": "Chat creado exitosamente"}, 200)
        
        return response
      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
      

@Chat.route("/chats")    
class Chats(Resource):
    @Chat.doc(params={'id_empleador': 'ID del empleador', 'id_empleado': 'ID del empleado'})
    def get(self):
      try:

        parser = Chat.parser()
        args = parser.parse_args()
        id_empleador = args.get('id_empleador')
        id_empleado = args.get('id_empleado')
        # Obtén el valor del parámetro id_empleador desde request.args
        session = db.session()

        # Realizar la consulta
        resultados = session.query(tbl_aichamba_chat).filter(
        tbl_aichamba_chat.aich_int_id_empleado == id_empleado,
        tbl_aichamba_chat.aich_int_id_empleador == id_empleador
        ).order_by(tbl_aichamba_chat.aich_date_fecha.asc()).all()
        
        # Construir una lista de diccionarios
        chats_list = [resultado.to_dict() for resultado in resultados]

        # Convertir la lista a formato JSON y devolver como respuesta
        json_response = jsonify({"response": chats_list})
        return(json_response)


      except Exception as e:
        error_message = {"error": str(e)}
        print(e)
        return error_message, 500
