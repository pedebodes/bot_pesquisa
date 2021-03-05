from resources import *
from flask import Flask,  request
from flask_restful import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(DominiosIgnorados, '/dominios_ignorar/')
api.add_resource(DominiosIgnoradosRemove,
                 '/dominios_ignorar/<int:url_id>/')

api.add_resource(PesquisaList, '/termos_pesquisados/')
api.add_resource(Pesquisa, '/pesquisa/')
