from sqlalchemy import ForeignKey
from ...Utils.db import db
from sqlalchemy.orm import relationship


class tbl_aichamba_trabajos(db.Model):
    aich_int_idtrabajos =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    aich_int_idempleador = db.Column(db.Integer, ForeignKey('tbl_aichamba_empleador.aich_int_idempleador') , nullable=False)
    aich_bit_estado = db.Column(db.Integer, nullable=False)


    empleador = relationship('tbl_aichamba_empleador', foreign_keys=[aich_int_idempleador])

    def to_dict(self):
        return {
            "aich_int_idtrabajos": self.aich_int_idtrabajos,
            "aich_int_idempleador": self.aich_int_idempleador,
            "aich_bit_estado": self.aich_bit_estado
        }

    def __init__(self, idempleador, estado):
        self.aich_int_idempleador = idempleador
        self.aich_bit_estado = estado

    def __repr__(self):
        return f'<tbl_aichamba_trabajos {self.aich_int_idtrabajos}>'