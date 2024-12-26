from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class IkiTopla(Resource):
    def get(self):
        sonuc = 2 + 2
        return {'sonuc': sonuc}, 200

class Carp(Resource):
    def get(self):
        return {'bilgi': 'Bu uç nokta çarpma işlemi yapmak için POST isteği bekliyor.'}, 200

    def post(self):
        try:
            veri = request.get_json() 
            if not veri or 'sayilar' not in veri:
                return {'hata': 'Lütfen "sayilar" anahtarını JSON içinde gönderin.'}, 400
            
            sayilar = veri.get('sayilar', [])
            if not all(isinstance(sayi, (int, float)) for sayi in sayilar):
                return {'hata': '"sayilar" listesi yalnızca sayılardan oluşmalıdır.'}, 400
            
            sonuc = 1
            for sayi in sayilar:
                sonuc *= sayi  
            return {'sonuc': sonuc}, 200
        except Exception as e:
            return {'hata': str(e)}, 500

api.add_resource(IkiTopla, '/iki_topla')
api.add_resource(Carp, '/carp')

if __name__ == '__main__':
    app.run(port=6900, host='0.0.0.0')
