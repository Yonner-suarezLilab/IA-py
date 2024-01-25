from ...Utils.db import db
from sqlalchemy.orm import relationship


class tbl_aichamba_notificacion_empleador(db.Model):
    aich_int_idnotificacion_empleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aich_vch_mensaje_notificacion = db.Column(db.Text, nullable = False)
    aich_vch_idempleado = db.Column(db.Integer, db.ForeignKey('tbl_aichamba_empleado.aich_int_idempleado'), nullable=False)
    aich_vch_idempleador = db.Column(db.Integer, db.ForeignKey('tbl_aichamba_empleador.aich_int_idempleador'), nullable=False)
    aich_bit_activo = db.Column(db.Integer, nullable=False)


    # Agregamos las relaciones
    empleado = relationship('tbl_aichamba_empleado', foreign_keys=[aich_vch_idempleado])
    empleador = relationship('tbl_aichamba_empleador', foreign_keys=[aich_vch_idempleador])

    def to_dict(self):
        return {
            "aich_int_idnotificacion_empleado": self.aich_int_idnotificacion_empleado,
            "aich_vch_mensaje_notificacion": self.aich_vch_mensaje_notificacion,
            "aich_vch_idempleado": self.aich_vch_idempleado,
            "aich_vch_idempleador": self.aich_vch_idempleador,
            "aich_bit_activo": self.aich_bit_activo
        }

    def __init__(self, mensaje_notificacion, idempleado, idempleador, activo):
        self.aich_vch_mensaje_notificacion = mensaje_notificacion
        self.aich_vch_idempleado = idempleado
        self.aich_vch_idempleador = idempleador
        self.aich_bit_activo = activo

    def __repr__(self):
        return f'<tbl_aichamba_notificacion_empleado {self.aich_int_idnotificacion_empleado}>'