
import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparse
from urllib.parse import urlencode
import json

class CarService:
    url = "https://www.cars.com/for-sale/searchresults.action/"
    def get_url(self, page=1, per_page=50, **kwargs):
        params = {
            'page': page,
            'perPage': per_page
        }
        
        if 'extcolor' in kwargs.keys():
            params['clrId'] = kwargs.get('extcolor')
        if 'brand' in kwargs.keys():
            params['mkId'] = kwargs.get('brand')
        if 'trans' in kwargs.keys():
            params['transTypeId'] = kwargs.get('trans')
        if 'year' in kwargs.keys():
            params['yrId'] = kwargs.get('year')
        url_parts = list(urlparse.urlparse(self.url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)

        url_parts[4] = urlencode(query)

        url = urlparse.urlunparse(url_parts)
       
        return url
    def get_cars(self, page=1, per_page=50, **kwargs):
        """
        internetten arabalari ceker ve liste halinde doner.
        """
        url=self.get_url(page, per_page, **kwargs)

        r = requests.get(url, headers={'User-Agent': 'Mozilla'}).content
        soup = BeautifulSoup(r, "html.parser")

        # filter_color_list=soup.find("li",{"id":"clrId"}).find_all("input")
        # color_dict={}
        # for i in filter_color_list:
        #     key = i['value']
        #     value = json.loads(i['data-dtm'])['value']
        #     color_dict[key] = value
        # print(color_dict)

        liste = soup.find_all(
            "div", {"class": "shop-srp-listings__listing-container"}, limit=50)
        # print(list)
        data = []

        for div in liste:
            title = div.a.div.h2.text.strip()
            price = div.find(
                "span", {"class": "listing-row__price"}).text.strip().strip("$")
            # image=div.find("div",{"class":"photo-scroll-wrapper"}).find_all("div")
            # del image[1]
            # print(image)
            brand = title.split()[1]
            year = title.split()[0]
            color = div.find(
                "ul", {"class": "listing-row__meta"}).find_all("li")[0].text.strip().split()[2]
            transmission = div.find(
                "ul", {"class": "listing-row__meta"}).find_all("li")[2].text.strip().split()[1]

            data.append({"title": title, "price": price, "brand": brand,
                         "year": year, "color": color, "trans": transmission})
        return data
