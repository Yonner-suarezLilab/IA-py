from app.models.Chats.tbl_aichamba_chat import tbl_aichamba_chat
from datetime import datetime
def crear_chat (data): 
    nuevoChat = tbl_aichamba_chat(id_empleado=data.get("id_empleado"), id_empleador=data.get("id_empleador"), mensaje=data.get("mensaje"), emisor=data.get("emisor"), receptor=data.get("receptor"), fecha=datetime.now(), estado=1 )

    return nuevoChat