from flask import Flask

from .extensions import api
from .resources import ns

# secret key open ia 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

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    api.add_namespace(ns)
    return app





