from ...Utils.db import db


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class tbl_aichamba_chat_relacion(db.Model):
    aich_int_id_chat_relacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aich_int_id_empleado = db.Column(db.Integer, ForeignKey('tbl_aichamba_empleado.aich_int_idempleado'))
    aich_int_id_empleador = db.Column(db.Integer, ForeignKey('tbl_aichamba_empleador.aich_int_idempleador'))
    aich_int_id_chat_empleado = db.Column(db.Integer, ForeignKey('tbl_aichamba_chat_empleado.aich_int_id_chat_empleado'))
    aich_int_id_chat_empleador = db.Column(db.Integer, ForeignKey('tbl_aichamba_chat_empleador.aich_int_id_chat_empleador'))

    empleado = relationship('tbl_aichamba_empleado', backref='chat_relacionados', foreign_keys=[aich_int_id_empleado])
    empleador = relationship('tbl_aichamba_empleador', backref='chat_relacionados', foreign_keys=[aich_int_id_empleador])
    chat_empleado = relationship('tbl_aichamba_chat_empleado', backref='chat_relacionados', foreign_keys=[aich_int_id_chat_empleado])
    chat_empleador = relationship('tbl_aichamba_chat_empleador', backref='chat_relacionados', foreign_keys=[aich_int_id_chat_empleador])

    def to_dict(self):
        return {
            "id_chat_relacion": self.aich_int_id_chat_relacion,
            "id_empleado": self.aich_int_id_empleado,
            "id_empleador": self.aich_int_id_empleador,
            "id_chat_empleado": self.aich_int_id_chat_empleado,
            "id_chat_empleador": self.aich_int_id_chat_empleador
        }

    def __init__(self, id_empleado, id_empleador, id_chat_empleado, id_chat_empleador):
        self.aich_int_id_empleado = id_empleado
        self.aich_int_id_empleador = id_empleador
        self.aich_int_id_chat_empleado = id_chat_empleado
        self.aich_int_id_chat_empleador = id_chat_empleador

    def __repr__(self):
        return f'<tbl_aichamba_chat_relacion {self.aich_int_id_chat_relacion}>'
