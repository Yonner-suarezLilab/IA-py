from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from ...Utils.db import db

class tbl_aichamba_chat(db.Model):
    __tablename__ = 'tbl_aichamba_chat'

    aich_int_id_chat = Column(Integer, primary_key=True, autoincrement=True)
    aich_int_id_empleado = Column(Integer, ForeignKey('tbl_aichamba_empleado.aich_int_idempleado'), nullable=False)
    aich_int_id_empleador = Column(Integer, ForeignKey('tbl_aichamba_empleador.aich_int_idempleador'), nullable=False)
    aich_vch_mensaje = Column(Text, nullable=True)
    aich_int_emisor = Column(Integer, nullable=False)
    aich_int_receptor = Column(Integer, nullable=False)
    aich_date_fecha = Column(Text, nullable=False)
    aich_bit_estado = Column(Integer, nullable=False)

    empleado = relationship('tbl_aichamba_empleado', backref='chat_relacionados_empleado', foreign_keys=[aich_int_id_empleado])
    empleador = relationship('tbl_aichamba_empleador', backref='chat_relacionados_empleador', foreign_keys=[aich_int_id_empleador])

    def to_dict(self):
        return {
            "id_chat": self.aich_int_id_chat,
            "id_empleado": self.aich_int_id_empleado,
            "id_empleador": self.aich_int_id_empleador,
            "mensaje": self.aich_vch_mensaje,
            "emisor": self.aich_int_emisor,
            "receptor": self.aich_int_receptor,
            "fecha": self.aich_date_fecha,
            "estado": self.aich_bit_estado
        }

    def __init__(self, id_empleado, id_empleador, mensaje, emisor, receptor, fecha, estado):
        self.aich_int_id_empleado = id_empleado
        self.aich_int_id_empleador = id_empleador
        self.aich_vch_mensaje = mensaje
        self.aich_int_emisor = emisor
        self.aich_int_receptor = receptor
        self.aich_date_fecha = fecha
        self.aich_bit_estado = estado

    def __repr__(self):
        return f'<tbl_aichamba_chat {self.aich_int_id_chat}>'

