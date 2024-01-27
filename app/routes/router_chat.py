from ..models.Intermedios.tbl_aichamba_chat_relacion import tbl_aichamba_chat_relacion
from ..models.Empleado.tbl_aichamba_chat_empleado import tbl_aichamba_chat_empleado
from ..models.Empleador.tbl_aichamba_chat_empleador import tbl_aichamba_chat_empleador
from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado
from ..models.Empleador.tbl_aichamba_empleador import tbl_aichamba_empleador
from ..logic.crear_chat_empleador import crear_chat_empleador
from ..logic.crear_chat_empleado import crear_chat_empleado
from ..logic.crear_relacion_chats import crear_relacion_chats
from flask import jsonify, request, make_response
from ..api_models import nuevo_chat
from flask_restx import Resource, Namespace
from ..Utils.db import db


Chat = Namespace("Chats")

@Chat.route("/chat_con_empleado")
class Chat_con_empleado(Resource):
    @Chat.expect(nuevo_chat)
    def post(self):
      try:
        data = request.json

        nuevo_chat_empleador = crear_chat_empleador(data)
        db.session.add(nuevo_chat_empleador)
        nuevo_chat_empleado = crear_chat_empleado(data)
        db.session.add(nuevo_chat_empleado)
        db.session.commit()


        nueva_relacion_chats = crear_relacion_chats(data, nuevo_chat_empleado.aich_int_id_chat_empleado, nuevo_chat_empleador.aich_int_id_chat_empleador)


        # Agrega y guarda en la base de datos
        db.session.add(nueva_relacion_chats)

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
      #try:

        parser = Chat.parser()
        args = parser.parse_args()
        id_empleador = args.get('id_empleador')
        id_empleado = args.get('id_empleado')
        # Obtén el valor del parámetro id_empleador desde request.args
        session = db.session()

        resultados = (
        session.query(
        tbl_aichamba_chat_empleado,
        tbl_aichamba_chat_empleador,
        tbl_aichamba_chat_relacion,
        tbl_aichamba_empleado,
        tbl_aichamba_empleador
    )
    .join(
        tbl_aichamba_chat_relacion,
        tbl_aichamba_chat_empleado.aich_int_id_empleado == tbl_aichamba_chat_relacion.aich_int_id_empleado
    )
    .join(
        tbl_aichamba_chat_empleador,
        tbl_aichamba_chat_relacion.aich_int_id_empleador == tbl_aichamba_chat_empleador.aich_int_id_empleador
    )
    .join(
        tbl_aichamba_empleado,
        tbl_aichamba_empleado.aich_int_idempleado == tbl_aichamba_chat_relacion.aich_int_id_empleado
    )
    .join(
        tbl_aichamba_empleador,
        tbl_aichamba_empleador.aich_int_idempleador == tbl_aichamba_chat_relacion.aich_int_id_empleador
    )
    # .filter(
    #     tbl_aichamba_chat_empleado.aich_int_id_empleado == id_empleado,
    #     tbl_aichamba_chat_empleador.aich_int_id_empleador == id_empleador,
    #     tbl_aichamba_empleado.aich_int_idempleado == id_empleado,
    #     tbl_aichamba_empleador.aich_int_idempleador == id_empleador
    # )
    .all()
)


        data = [
    {
        "mensaje_empleador": chat_empleador.aich_vch_mensaje,
        "nombre_empleador": empleador.aich_vch_nombre,
        "id_empleador": empleador.aich_int_idempleador,
        "mensaje_empleado": chat_empleado.aich_vch_mensaje,
        "nombre_empleado": empleado.aich_vch_nombre,
        "id_empleado": empleado.aich_int_idempleado,
    }
    for chat_empleado, chat_empleador, relacion, empleado, empleador in resultados
]

        return jsonify({"response": data})

      # except Exception as e:
      #   error_message = {"error": str(e)}
      #   print(e)
      #   return error_message, 500
    
    ##

