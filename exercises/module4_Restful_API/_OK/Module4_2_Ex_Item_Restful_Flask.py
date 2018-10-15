#reource routing and endpoint
from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

items = {}

class Item(Resource):
    def get(self,item_id):
        return {item_id: items[item_id]}

    def put(self, item_id):
        print(request.form['name'])
        print(request.form['qty'])
        product={}
        product['name']=request.form['name']
        product['qty']=request.form['qty']        
        items[item_id]= product
        return {item_id: items[item_id]}

api.add_resource(Item, '/<string:item_id>')

if __name__ == '__main__':
    app.run(debug=True)