from ..models.Empleador.tbl_aichamba_notificacion_empleador import tbl_aichamba_notificacion_empleador


def create_notificacion_empleador_from_json(data):
    nueva_notificacion = tbl_aichamba_notificacion_empleador(
        mensaje_notificacion=data.get("mensaje_notificacion"),
        idempleado=data.get("idempleado"),
        idempleador=data.get("idempleador"),
        activo=1
      )

    return nueva_notificacion
