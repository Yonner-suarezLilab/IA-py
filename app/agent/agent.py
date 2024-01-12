import openai
from instantneo.core import InstantNeo
from app.Utils.DataEmpleados import DataEmpleado
from app.Utils.DataEmpleador import DataEmpleador


def create_agent():
    system_role = f"""
        Instrucción 1: Recibirás una pregunta y deberás responderla basandote en estos datos {DataEmpleado}.
        Deberás responder con la información que se te pide de manera breve y concisa.
        """

    model = "gpt-3.5-turbo-16k"

    api_key=""

    return InstantNeo(
            api_key = api_key,
            model = model,
            role_setup = system_role,
            max_tokens = 2000,
            temperature = 0.5,
            skills = [],
            )