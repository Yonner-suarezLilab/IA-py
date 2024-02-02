from ...Utils.InstantNeo import InstantNeo
from ...config import api_key_ia, default_model

def agentMatch():
      role = """
      Tu deber buscar en una lista de trabajadores, el mas indicadl para el puesto de trabajo que tienes disponible.
      La busqueda son una evaluacion con criterio entre los siguientes valores: [Reputacion], [Resumen] y [TrabajosRealizados].
      
      return: Deberas dar una la lista de los primeros 10 trabajadores con mayor capacidad de cubrir el trabajo.
              La lista la devolveras en un formato JSON. Con ID y nombre del trabajador.
              Alprincipio de la lista deberas poner el trabajador con mayor capacidad.
              Dentro de este JSON habra mensaje y lista. La lista sera un array de objetos con el ID y nombre del trabajador.
              Y el mensaje sera un string con la explicacion por que elegiste al trabajador y si queres recomendar a otro ademas de ese (opcional).
      """
      agent = InstantNeo(
          api_key=api_key_ia,
          model=default_model,
          role_setup=role,
          max_tokens=1000,
          temperature=0.7,
          #skills=[]
      )
      return agent