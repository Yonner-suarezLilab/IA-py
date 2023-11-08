from flask import Flask

from .extensions import api
from .resources import ns
import openai

# secret key open ia 

openai.api_key="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"

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    api.add_namespace(ns)
    return app





