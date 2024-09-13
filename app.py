from django.http import HttpResponse
from flask import Flask
from flask_restful import Resource, Api
import main

app = Flask(__name__)
api = Api(app)

class Startups(Resource):
    def get(self):
        return  {"startups":[
            {"bovespa": {
                "inovacao": "baixa",
                "gtp": main.mensagem
            }

             },
            {"nubank": {
                "inovacao":"alta",
                "gpt":main.mensagem
            }}
        ]
        }


api.add_resource(Startups,'/startups')

if __name__ == '__main__':
    app.run(debug=True)