from flask_restx import fields

from .extensions import api


nuevo_empleado = api.model("request", {
    "Name": fields.String,
    "Email": fields.String
})


nuevo_empleador = api.model("nuevo_empleador", {
    "Nombre": fields.String(required=True, description="Nombre del empleador"),
    "Email": fields.String(required=True, description="Correo electrónico del empleador"),
    "Apellido": fields.String(description="Apellido del empleador"),
    "Documento": fields.Integer(description="Documento del empleador"),
    "Direccion": fields.String(description="Dirección del empleador"),
    "Telefono": fields.String(description="Teléfono del empleador"),
    "Foto": fields.String(description="URL de la foto del empleador"),
    "Rol": fields.String(description="Rol del empleador")  
})
