from ..Utils.db import db 


# Definir modelos aquí
class tbl_aichamba_empleador(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    IdEmpleador = db.Column(db.Integer, nullable=False)
    apellido = db.Column(db.String(80))
    Documento = db.Column(db.Integer)
    Direccion = db.Column(db.String(120))
    CP = db.Column(db.Integer)
    Telefono = db.Column(db.Integer)
    Foto = db.Column(db.String(120))
    Rol = db.Column(db.String(80))

    def __init__(self, nombre, email, IdEmpleador, apellido, Documento, Direccion, CP, Telefono, Foto, Rol):
        self.nombre = nombre
        self.email = email
        self.IdEmpleador = IdEmpleador
        self.apellido = apellido
        self.Documento = Documento
        self.Direccion = Direccion
        self.CP = CP
        self.Telefono = Telefono
        self.Foto = Foto
        self.Rol = Rol

    def __repr__(self):
        return f'<EmployerDB {self.nombre}>'


# Definir modelos aquí
class EmployerProposal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('tbl_aichamba_empleador.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80))
    photo = db.Column(db.String(120))
    description = db.Column(db.Text)

    def __init__(self, employer_id, name, last_name, photo, description):
        self.employer_id = employer_id
        self.name = name
        self.last_name = last_name
        self.photo = photo
        self.description = description

    def __repr__(self):
        return f'<EmployerProposal {self.name}>'

