from flask import make_response, request, json
from flask_restx import Resource, Namespace
from ..api_models import request_match, request_jobee
from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado
from ..logic.IA.crear_agent import agentMatch
from ..logic.IA.jobee import agentJobee

IA = Namespace("IA")

@IA.route("/Match_empleado")
class Match_empleado(Resource):
  @IA.expect(request_match)
  def post(self):

    data = request.json 

    mensaje = data.get("peticion_match")  

    empleados = tbl_aichamba_empleado.query.all()
    agente = agentMatch()
    match = agente.run(f'{empleados}. {mensaje}') 
    
    # empleados_json = [empleado.to_dict() for empleado in empleados]
    #   

    response = make_response({"match": match }, 200)
    return response


@IA.route("/Jobee")
class Agent_jobee(Resource):
  @IA.expect(request_jobee)
  def post(self):

    data = request.json

    mensaje = data.get("pregunta")

    agente_jobee = agentJobee()
    result = agente_jobee.run(f'{mensaje}')