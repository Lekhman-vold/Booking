import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():

    from app.models import register_models
    from app.routes import register_routes
    from app.models.facility import Room, Booking
    from app.models.user import User

    app = Flask(__name__)

    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SECURITY_PASSWORD_SALT'] = os.getenv("SECURITY_PASSWORD_SALT")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

    JWTManager(app)

    db.init_app(app)

    admin = Admin(app, name='Booking system', template_mode='bootstrap4')
    admin.add_view(ModelView(Room, db.session))
    admin.add_view(ModelView(Booking, db.session))
    admin.add_view(ModelView(User, db.session))

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error!"
        }), 500

    app.db = db

    migrate.init_app(app, db)

    api = Api(app, title="Booking API", version="0.1.0")

    register_models()
    register_routes(api, app)

    return app
