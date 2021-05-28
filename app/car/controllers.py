
from app.car.services import CarService
from flask import Blueprint, json, request
from flask_restful import Resource, Api,fields, marshal_with,marshal
from app import cache,app

car = Blueprint('car', __name__, url_prefix='/cars')

api = Api(car)

carsevice = CarService()       


resource_fields = {
    'title': fields.String,
    'price': fields.String,
    'brand' : fields.String,
    'year': fields.String,
    'color':fields.String,
    'trans' : fields.String,
}

class Car(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        """
        Kwargs: 
            extcolor: rengi belirtir.
            brand: modeli belirtir.
            trans: vites türünü belirtir.
            year: yilini belirtir. 
        """
        
        
        url = carsevice.get_url(
                request.args.get('page'),
                request.args.get('per_page'),
                **request.args
            )
        is_cached = request.args.get('cache')
        if  is_cached != '0':
            
            print(url)
            d = cache.get(url)
            if d != None:
                return json.loads(d)

        data = carsevice.get_cars(**request.args)
       
        cache.set(url,json.dumps(data), timeout=app.config['CACHE_DEFAULT_TIMEOUT'])

        


        return data



api.add_resource(Car, '/')


              