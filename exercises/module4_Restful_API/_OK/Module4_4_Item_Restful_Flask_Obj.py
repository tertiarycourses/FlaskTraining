#reource routing and endpoint
from flask import Flask, request
from flask_restful import Resource, Api
import json
from flask_restful import fields, marshal_with
import json

resource_fields = {
    'name':   fields.String,
    'qty':    fields.Integer,
    'uri':    fields.Url('item_ep')
}

app = Flask(__name__)
api = Api(app)

items = {}

class MyProduct(object):
    def __init__(self, pitem_id, pname, pqty):
        self.my_iten_id = pitem_id
        self.my_name = pname
        self.my_qty= pqty

        # This field will not be sent in the response
        self.status = 'active'

class Item(Resource):
    #@marshal_with(resource_fields)
    def get(self, item_id):
        i= items[item_id]
        print(i)
        print("---"+i['name'])
        print("---"+i['qty'])
        myobj= MyProduct(item_id,i['name'],i['qty'] )
        print(myobj.my_name)
        a= json.dumps(myobj.__dict__)
        #return {item_id: items[item_id]}
        return a

    def put(self, item_id):
        print(request.form['name'])
        print(request.form['qty'])
        product={}
        product['name']=request.form['name']
        product['qty']=request.form['qty']        
        items[item_id]= product
        return {item_id: items[item_id]}

api.add_resource(Item, '/<string:item_id>', endpoint='item_ep')

if __name__ == '__main__':
    app.run(debug=True)