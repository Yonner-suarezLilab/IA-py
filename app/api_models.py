from flask_restx import fields

from .extensions import api


requestIA = api.model("request", {
    "Question": fields.String
})