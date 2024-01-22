from ..Utils.db import db 


# Definir modelos aquí
class EmployerDB(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
  def __repr__(self):
      return f'<EmployerDB {self.nombre}>'