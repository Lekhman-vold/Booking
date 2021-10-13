from flask_restx import Namespace, Resource

# from flask_jwt_extended import jwt_required

api = Namespace("ClientRentalApi", description="Client requests")


@api.route('/')
class TestRoute(Resource):
    def get(self):
        return "worked!"
