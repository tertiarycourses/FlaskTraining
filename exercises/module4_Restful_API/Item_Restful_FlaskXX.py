from cerberus import Validator
from datetime import datetime
#from uuid import uuid64
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# items = {{'one':{'name':'milk','quantity':20,'date_created':"",'date_modified':""}},}
items={}

class SingleItem(Resource):
    def get(self, id):
        try:
            item = items[id]
        except IndexError:
            return "Item could not be found", 404
        return item

    def put(self, id):
        try:
            print("------------------------"+id)
            item = items[id]
            print(item)
        except IndexError:
            return "Item could not be found", 404
        body = request.json
        item['name'] = body['name'] or item['name']
        item['quantity'] = body['quantity'] or item['quantity']
        item['date_created'] = datetime.now()
        item['date_modified'] = datetime.now()

        # We shall be validating the request body data against this
        schema = {
            'name': {'required': 'True', 'type': 'string'},
            'quantity': {'type': 'integer', 'min': 10},
            'date_created': {'type': 'datetime'},
            'date_modified': {'type': 'datetime'}
        }
        v = Validator(schema)
        if not v(item):
            return "There was something wrong with your arguments", 400

        item[id] = id
        items[id] = item
        return item

    def delete(self, id):
        try:
            item = items[id]
        except IndexError:
            return "Item could not be found", 404
        return "Item has been deleted", 204

api.add_resource(SingleItem, '/items/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)