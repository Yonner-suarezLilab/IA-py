from ...Utils.db import db

class tbl_aichamba_chat_empleador(db.Model):
    aich_int_id_chat_empleador =  db.Column(db.Integer, primary_key=True, autoincrement=True) 
    aich_int_id_empleador =  db.Column(db.Integer, nullable=False)
    aich_vch_mensaje =  db.Column(db.Text, nullable = False)
    aich_bit_estado = db.Column(db.Integer, nullable = False)

    def to_dict(self):
        return {
            "id_chat_empleador": self.aich_int_id_chat_empleador,
            "id_empleador": self.aich_int_id_empleador,
            "mensaje": self.aich_vch_mensaje,
            "estado": self.aich_bit_estado
        }

    def __init__(self, id_empleador, mensaje, estado):
        self.aich_int_id_empleador = id_empleador
        self.aich_vch_mensaje = mensaje
        self.aich_bit_estado = estado

    def __repr__(self):
        return f'<tbl_aichamba_chat_empleador {self.aich_int_id_chat_empleador}>'