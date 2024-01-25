from ...Utils.db import db 


class tbl_aichamba_empleador(db.Model):
    aich_int_idempleador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aich_vch_nombre = db.Column(db.String(80), nullable=False)
    aich_vch_email = db.Column(db.String(120), unique=True, nullable=False)
    aich_vch_apellido = db.Column(db.String(80))
    aich_vch_documento = db.Column(db.Integer)
    aich_vch_direccion = db.Column(db.String(120))
    aich_vch_telefono = db.Column(db.String(20))
    aich_vch_foto = db.Column(db.String(120))
    aich_vch_rol = db.Column(db.String(80))
    aich_bit_activo = db.Column(db.Integer)

    def to_dict(self):
        return {
            "aich_int_idempleador": self.aich_int_idempleador,
            "aich_vch_nombre": self.aich_vch_nombre,
            "aich_vch_email": self.aich_vch_email,
            "aich_vch_apellido": self.aich_vch_apellido,
            "aich_vch_documento": self.aich_vch_documento,
            "aich_vch_direccion": self.aich_vch_direccion,
            "aich_vch_telefono": self.aich_vch_telefono,
            "aich_vch_foto": self.aich_vch_foto,
            "aich_vch_rol": self.aich_vch_rol,
            "aich_bit_activo": self.aich_bit_activo
        }

    def __init__(self, nombre, email, apellido, documento, direccion, telefono, foto, rol, activo):
        self.aich_vch_nombre = nombre
        self.aich_vch_email = email
        self.aich_vch_apellido = apellido
        self.aich_vch_documento = documento
        self.aich_vch_direccion = direccion
        self.aich_vch_telefono = telefono
        self.aich_vch_foto = foto
        self.aich_vch_rol = rol
        self.aich_bit_activo = activo

    def __repr__(self):
        return f'<tbl_aichamba_empleador {self.aich_vch_nombre}>'



    ##1 notificacion
    ##1 empleado Ya esta
    ##1 

    ##empleador
    ##1 tiene varios trabajos/publicaciones    idempleados postulantes relacion vfarios a varios si ya se hizo va en 1 si no va en 0
    ##

    ##1 empleador tien una notificacion con el id empleado/postulante


    ##tabla chat para empleador


    ##notificaciones empleado frangmento de chat si es ia