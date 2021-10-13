from flask import jsonify, request, make_response
from flask_restx import Namespace, Resource
from flask_jwt_extended import create_access_token, get_jwt_identity, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db

api = Namespace("LoginRentalApi", description="Login requests")


@api.route('/login')
class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = db.session.query(User).filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({
                "status": "failed",
                "message": "Failed getting user"
            }), 401

        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        return make_response(
            jsonify({
                "status": "success",
                "message": "auth successfully",
                "data": {
                    "id": user.id,
                    "access_token": access_token,
                    "email": user.email,
                    "refresh_token": refresh_token
                }
            }), 200
        )


@api.route('/register')
class Register(Resource):
    def post(self):
        data = request.get_json()

        if data is None:
            return make_response(
                jsonify({
                    "status": "error",
                    "message": "data is not None"
                }), 422
            )

        try:
            email = data.get("email")
            password = generate_password_hash(data.get("password"))
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            role_id = data.get("role_id")

            new_user = User(email=email,
                            password_hash=password,
                            first_name=first_name,
                            last_name=last_name,
                            role_id=role_id)
            db.session.add(new_user)
            db.session.commit()

            return make_response(
                jsonify({
                    "status": "success",
                    "message": "User added successfully"
                }), 201
            )

        except Exception as e:
            return make_response(
                jsonify({
                    "status": "Error",
                    "message": f"{e}"
                }), 422
            )

