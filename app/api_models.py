from flask_restx import fields

from .extensions import api


new_Employee = api.model("request", {
    "Name": fields.String,
    "Email": fields.String
})

