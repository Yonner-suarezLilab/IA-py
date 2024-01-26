from ...Utils.db import db


class tbl_aichamba_empleado(db.Model):
    aich_int_idempleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aich_vch_nombre = db.Column(db.String(80), nullable=False)
    aich_vch_email = db.Column(db.String(120), unique=True, nullable=False)
    aich_vch_apellido = db.Column(db.String(80))
    aich_vch_documento = db.Column(db.Integer)
    aich_vch_ocupacion = db.Column(db.String(80))
    aich_vch_reputacion = db.Column(db.String(10))
    aich_vch_direccion = db.Column(db.String(120))
    aich_vch_telefono = db.Column(db.String(120))
    aich_vch_imagen = db.Column(db.Text)
    aich_vch_rol = db.Column(db.String(80))
    aich_vch_trabajos_realizados = db.Column(db.Integer)
    aich_vch_Resumen = db.Column(db.Text)
    aich_bit_activo = db.Column(db.Integer)


    def to_dict(self):
        return {
            "aich_int_idempleado": self.aich_int_idempleado,
            "aich_vch_nombre": self.aich_vch_nombre,
            "aich_vch_email": self.aich_vch_email,
            "aich_vch_apellido": self.aich_vch_apellido,
            "aich_vch_documento": self.aich_vch_documento,
            "aich_vch_ocupacion": self.aich_vch_ocupacion,
            "aich_vch_reputacion": self.aich_vch_reputacion,
            "aich_vch_direccion": self.aich_vch_direccion,
            "aich_vch_telefono": self.aich_vch_telefono,
            "aich_vch_imagen": self.aich_vch_imagen,
            "aich_vch_rol": self.aich_vch_rol,
            "aich_vch_trabajos_realizados": self.aich_vch_trabajos_realizados,
            "aich_vch_Resumen": self.aich_vch_Resumen,
            "aich_bit_activo": self.aich_bit_activo
        }

    def __init__(self, nombre, email, apellido, documento, ocupacion, reputacion, direccion, telefono, imagen, rol, trabajos_realizados, resumen):
        self.aich_vch_nombre = nombre
        self.aich_vch_email = email
        self.aich_vch_apellido = apellido
        self.aich_vch_documento = documento
        self.aich_vch_ocupacion = ocupacion
        self.aich_vch_reputacion = reputacion
        self.aich_vch_direccion = direccion
        self.aich_vch_telefono = telefono
        self.aich_vch_imagen = imagen
        self.aich_vch_rol = rol
        self.aich_vch_trabajos_realizados = trabajos_realizados
        self.aich_vch_Resumen = resumen
        self.aich_bit_activo = 1

    def __repr__(self):
        return f'<tbl_aichamba_empleado {self.aich_vch_nombre}>'


