from ..models.Empleado.tbl_aichamba_notificacion_empleado import tbl_aichamba_notificacion_empleado

def create_notificacion_empleado_from_json(data):
    nueva_notificacion = tbl_aichamba_notificacion_empleado(
        mensaje_notificacion=data.get("mensaje_notificacion"),
        idempleado=data.get("idempleado"),
        idempleador=data.get("idempleador"),
        activo=1
    )

    return nueva_notificacion
