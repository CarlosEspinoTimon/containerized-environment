"""
Server Module
"""
import sys

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


sys.stdout.flush()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .models.dish import Dish

    # Import blueprints
    from .controllers import dish_controller
    app.register_blueprint(dish_controller.dishes)

    # A simple page that says server status
    @app.route('/')
    def home():
        return jsonify('The server is running!!')

    return app
