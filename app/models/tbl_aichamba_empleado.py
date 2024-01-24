from ..Utils.db import db


# Definir modelos aquí
class tbl_aichamba_empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    IdEmpleado = db.Column(db.Integer, nullable=False)
    apellido = db.Column(db.String(80))
    Documento = db.Column(db.Integer)
    Ocupacion = db.Column(db.String(80))
    Reputacion = db.Column(db.String(10))
    Direccion = db.Column(db.String(120))
    CP = db.Column(db.Integer)
    Telefono = db.Column(db.Integer)
    Foto = db.Column(db.String(120))
    Rol = db.Column(db.String(80))
    TrabajosRealizados = db.Column(db.Integer)
    Resumen = db.Column(db.Text)

    def __init__(self, nombre, email, IdEmpleado, apellido, Documento, Ocupacion, Reputacion, Direccion, CP, Telefono, Foto, Rol, TrabajosRealizados, Resumen):
        self.nombre = nombre
        self.email = email
        self.IdEmpleado = IdEmpleado
        self.apellido = apellido
        self.Documento = Documento
        self.Ocupacion = Ocupacion
        self.Reputacion = Reputacion
        self.Direccion = Direccion
        self.CP = CP
        self.Telefono = Telefono
        self.Foto = Foto
        self.Rol = Rol
        self.TrabajosRealizados = TrabajosRealizados
        self.Resumen = Resumen

    def __repr__(self):
        return f'<EmployeeDB {self.nombre}>'
