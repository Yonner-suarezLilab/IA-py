from ...Utils.db import db

class tbl_aichamba_trabajos_postulaciones(db.Model):
    aich_int_trabajos_postulaciones = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aich_int_idtrabajo = db.Column(db.Integer, db.ForeignKey('tbl_aichamba_trabajos.aich_int_idtrabajos') ,nullable=False)
    aich_int_idempleado = db.Column(db.Integer, db.ForeignKey('tbl_aichamba_empleado.aich_int_idempleado') ,nullable=False)
    aich_bit_activo = db.Column(db.Integer, nullable = False)

    # Relación muchos a muchos con Trabajo y Empleado
    trabajo = db.relationship('tbl_aichamba_trabajos', foreign_keys=[aich_int_idtrabajo])
    empleado = db.relationship('tbl_aichamba_empleado',  foreign_keys=[aich_int_idempleado])

    def to_dict(self):
        return {
            "aich_int_trabajos_postulaciones": self.aich_int_trabajos_postulaciones,
            "aich_int_idtrabajo": self.aich_int_idtrabajo,
            "aich_int_idempleado": self.aich_int_idempleado,
            "aich_bit_activo": self.aich_bit_activo
        }

    def __init__(self, idtrabajo, idempleado, activo):
        self.aich_int_idtrabajo = idtrabajo
        self.aich_int_idempleado = idempleado
        self.aich_bit_activo = activo

    def __repr__(self):
        return f'<tbl_aichamba_trabajos_postulaciones {self.aich_int_trabajos_postulaciones}>'