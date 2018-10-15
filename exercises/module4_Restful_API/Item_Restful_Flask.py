from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        #todos[todo_id] = request.form['data']
        print(request.form['name'])
        print(request.form['qty'])
        product={}
        product['name']=request.form['name']
        product['qty']=request.form['qty']        
        todos[todo_id]= product
        # a= json.loads( request.form['data'])
        # print(a['name'])
        # print(a['qty'])
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)