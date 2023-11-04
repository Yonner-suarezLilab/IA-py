from flask_restx import Resource, Namespace
from flask import jsonify
from .api_models import requestIA
import openai

ns = Namespace("IA")



@ns.route("/requesttIA")
class RequestIA(Resource):
    @ns.expect(requestIA)
    def post(self):
        response = openai.Completion.create(
            engine = "gpt-3.5-turbo",
            prompt = requestIA,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequenzy_penalty = 0,
            presence_penalty = 0.6
        )

        answer = response.choices[0].text.strip()

        

        return jsonify({"response": answer})