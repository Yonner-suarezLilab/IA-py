from ..models.Intermedios.tbl_aichamba_chat_relacion import tbl_aichamba_chat_relacion



def crear_relacion_chats(data, nuevo_id_chat_empleado, nuevo_id_chat_empleador):
    
    nueva_relacion = tbl_aichamba_chat_relacion(
        id_empleado=data.get("id_empleado"),
        id_empleador=data.get("id_empleador"),
        id_chat_empleado = nuevo_id_chat_empleado,
        id_chat_empleador= nuevo_id_chat_empleador
    )

    return nueva_relacion
