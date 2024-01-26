from flask_restx import fields

from .extensions import api


nuevo_empleado = api.model("nuevo_empleado", {
    "Name": fields.String,
    "Email": fields.String,
    "Apellido": fields.String,
    "Documento": fields.Integer,
    "Ocupacion": fields.String,
    "Reputacion": fields.String,
    "Direccion": fields.String,
    "Telefono": fields.String,
    "Imagen": fields.String,
    "Rol": fields.String,
    "TrabajosRealizados": fields.Integer,
    "Resumen": fields.String,
    "Latitud": fields.String,
    "Longitud": fields.String
})



nuevo_empleador = api.model("nuevo_empleador", {
    "Nombre": fields.String(required=True, description="Nombre del empleador"),
    "Email": fields.String(required=True, description="Correo electrónico del empleador"),
    "Apellido": fields.String(description="Apellido del empleador"),
    "Documento": fields.Integer(description="Documento del empleador"),
    "Direccion": fields.String(description="Dirección del empleador"),
    "Telefono": fields.String(description="Teléfono del empleador"),
    "Foto": fields.String(description="URL de la foto del empleador"),
    "Rol": fields.String(description="Rol del empleador"),
    "Latitud": fields.String,
    "Longitud": fields.String
})


nueva_notificacion_empleado = api.model("NotificacionEmpleado", {
    "mensaje_notificacion": fields.String(description="Mensaje de la notificación", required=True),
    "idempleado": fields.Integer(description="ID del empleado", required=True),
    "idempleador": fields.Integer(description="ID del empleador", required=True),
})


nueva_notificacion_empleador = api.model("NotificacionEmpleador", {
    "mensaje_notificacion": fields.String(description="Mensaje de la notificación", required=True),
    "idempleado": fields.Integer(description="ID del empleado", required=True),
    "idempleador": fields.Integer(description="ID del empleador", required=True),
})

nuevo_trabajo = api.model("Trabajo",{
    "idEmpleador": fields.Integer,
    "Descripcion": fields.String
})

nueva_postulacion = api.model("Nueva_postulacion", {
    "id_trabajo": fields.Integer,
    "id_empleado": fields.Integer
})

postulantes_publicaciones = api.model("postulantes_publicaciones", {
    "id_trabajo": fields.Integer,
    "id_empleado": fields.Integer
})

notificar_postulacion = api.model("Notificar_Postulacion", {
    "mensaje_notificacion": fields.String(description="Mensaje de la notificación", required=True),
    "idempleado": fields.Integer(description="ID del empleado", required=True),
    "idempleador": fields.Integer(description="ID del empleador", required=True),
})