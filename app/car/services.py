from app.car.models import Car
from typing import List
import requests



class CarService:
    url = "https://www.cars.com/for-sale/searchresults.action"
    def get_cars(self, **kwargs) -> List[Car]:
        """
        internetten arabalari ceker ve liste halinde doner.
        """
        r = requests.get(self.url)
        
        return []

