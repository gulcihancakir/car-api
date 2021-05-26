from flask import Blueprint
from flask_restful import Resource, Api


car = Blueprint('car', __name__, url_prefix='/cars')

api = Api(car)
class Car(Resource):
    
    def get(self, **kwargs):
        """
        Args: 
            extcolor: rengi belirtir.
            brand: modeli belirtir.
            trans: vites türünü belirtir.
            year: yilini belirtir. 
        """
        return []
        



api.add_resource(Car, '/')


              