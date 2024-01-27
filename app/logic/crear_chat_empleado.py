from ..models.Empleado.tbl_aichamba_chat_empleado import tbl_aichamba_chat_empleado


def crear_chat_empleado(data):
    
    nuevo_chat = tbl_aichamba_chat_empleado(
        id_empleado=data.get("id_empleado"),
        mensaje=data.get(""),
        estado=1
    )

    return nuevo_chat

