from .app import app
from .Utils.db import db
from.extensions import api

# with app.app_context():
#   db.create_all()
@app.before_first_request
def create_database():
     db.create_all()

if __name__ == "__main__":
  app.run(debug=True)