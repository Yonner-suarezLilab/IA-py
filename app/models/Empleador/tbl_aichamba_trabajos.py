from sqlalchemy import ForeignKey
from ...Utils.db import db
from sqlalchemy.orm import relationship


class tbl_aichamba_trabajos(db.Model):
    aich_int_idtrabajos =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    aich_int_idempleador = db.Column(db.Integer, ForeignKey('tbl_aichamba_empleador.aich_int_idempleador') , nullable=False)
    aich_vch_descripcion = db.Column(db.Text, nullable=False)
    aich_vch_imagen =  db.Column(db.Text)
    aich_bit_estado = db.Column(db.Integer, nullable=False)
    aich_vch_latitud = db.Column(db.Text)
    aich_vch_longitud = db.Column(db.Text)


    empleador = relationship('tbl_aichamba_empleador', foreign_keys=[aich_int_idempleador])

    def to_dict(self):
        return {
            "aich_int_idtrabajos": self.aich_int_idtrabajos,
            "aich_int_idempleador": self.aich_int_idempleador,
            "aich_vch_descripcion": self.aich_vch_descripcion,
            "aich_bit_estado": self.aich_bit_estado,
            "aich_vch_imagen": self.aich_vch_imagen,
            "aich_vch_latitud": self.aich_vch_latitud,
            "aich_vch_longitud": self.aich_vch_longitud
        }

    def __init__(self, idempleador, descripcion, imagen, latitud, longitud):
        self.aich_int_idempleador = idempleador,
        self.aich_vch_descripcion = descripcion,
        self.aich_vch_imagen = imagen,
        self.aich_vch_latitud = latitud,
        self.aich_vch_longitud = longitud
        self.aich_bit_estado = 1

    def __repr__(self):
        return f'<tbl_aichamba_trabajos {self.aich_int_idtrabajos}>'