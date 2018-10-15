#Argument Parsing
from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse, abort
import json

app = Flask(__name__)
api = Api(app)

items = {}

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('qty', type=int, help='qty  for this resource')


class Item(Resource):
    def get(self,item_id):
        return {item_id: items[item_id]}

    def put(self, item_id):
        args = parser.parse_args()
        print(">>"+request.form['name'])
        print(">>>"+request.form['qty'])
        product={'name':args['name'],'qty':args['qty']}
     
        items[item_id]= product
        
        return {item_id: items[item_id]}

api.add_resource(Item, '/<string:item_id>')

if __name__ == '__main__':
    app.run(debug=True)