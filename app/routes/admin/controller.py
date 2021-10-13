from flask import request, jsonify, make_response
from flask_restx import Namespace, Resource
from app import db
from app.models.facility import Room, Booking
from flask_jwt_extended import jwt_required
from datetime import datetime, timedelta

api = Namespace("AdminRentalApi", description="Admin requests")


@api.route('/')
class TestRoute(Resource):
    @jwt_required()
    def get(self):
        return "worked"


@api.route('/reserve')
class ReserveFacility(Resource):
    def get(self):
        return ''

    # @jwt_required()
    def post(self):
        data = request.get_json()
        customer = data.get("customer")
        room_number = data.get("room_id")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        room = db.session.query(Room).filter_by(number=room_number).first()

        new_reserve = Booking(customer=customer,
                              room_number=room.id,
                              start_date=start_date,
                              end_date=end_date)
        room.is_booked = True

        db.session.add(new_reserve)
        db.session.add(room)
        db.session.commit()

        return make_response(
            jsonify({
                "status": "success",
                "message": "room booked."
            }), 201
        )


