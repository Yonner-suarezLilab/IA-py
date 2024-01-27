from..models.Empleador.tbl_aichamba_chat_empleador import tbl_aichamba_chat_empleador

def crear_chat_empleador(data):
    
  nuevo_chat = tbl_aichamba_chat_empleador(
    id_empleador=data.get("id_empleador"),
    mensaje=data.get("mensaje"),
    estado=1
  )

  return nuevo_chat


   