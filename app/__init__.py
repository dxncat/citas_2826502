from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

#crear objetode la aplicacion
app = Flask(__name__)

#configurar la app
app.config.from_object(Config)

#crear objeto sqlalchemy
db = SQLAlchemy(app)

#crear objeto para hacer migraciones
migrate = Migrate(app, db)

from .models import Medico

if __name__ == "__main__":
    app.run()