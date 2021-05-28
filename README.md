gerekli paketleri kurmak için

pip install -r requirements.txt

Verileri https://www.cars.com/for-sale/searchresults.action sitesinden alabilmek için requests kütüphanesini kullanarak istek attım.
Parse işlemi için de BeautifulSoup kullandım.Bunları services.py içerisinde yaptım.

Api için flask web framework'ü ve flask_restful kütüphanesini kullandım.

controllers.py içerisinde services.py dosyasından aldığım verileri json formatına dönüştürdüm.

Daha önce atılan bi istek tekrar atılıyor ise  ve hiç bir değişiklik olmadıysa verileri cache den alır.

