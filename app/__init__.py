
from app.car.services import CarService
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)

app.config.from_object('config')
cache = Cache(app)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.car.controllers import car

app.register_blueprint(car)

c = CarService()
c.get_cars()    


