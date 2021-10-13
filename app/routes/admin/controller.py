from flask import request, jsonify
from flask_restx import Namespace, Resource
from app import db
from app.models.facility import Facility, Rental
from flask_jwt_extended import jwt_required

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
        data = db.session.query(Facility)
        # data = data.query.join(Rental)
        print(data)
        return ''


