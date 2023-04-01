from flask import Flask
from .config import Config
from .utils.db import db
from .utils.schemas import ma
from .routes.station_api import station_api
from .routes.index import index

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Blueprints
    app.register_blueprint(station_api)
    app.register_blueprint(index)
 
    # SQLAlchemy and Marshmallow settings
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    return app