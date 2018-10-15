from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TITEMS = {
    'items1': {'name': 'milk','qty':10},
    'items2': {'name': 'egg','qty':100},
    'items3': {'name': 'drink','qty':30},
}


def abort_if_item_doesnt_exist(item_id):
    if item_id not in TITEMS:
        abort(404, message="Item {} doesn't exist".format(item_id))

parser = reqparse.RequestParser()
parser.add_argument('name')


# Todo
# shows a single todo item and lets you delete a todo item
class Item(Resource):
    def get(self, item_id):
        abort_if_item_doesnt_exist(item_id)
        return TITEMS[item_id]

    def delete(self, item_id):
        abort_if_item_doesnt_exist(item_id)
        del TITEMS[item_id]
        return '', 204

    def put(self, item_id):
        args = parser.parse_args()
        body = request.json
        # product = {'name': args['name']}
        product={'name':body['name'],'qty':body['qty']}
        TITEMS[item_id] = product
        return task, 201


# # TodoList
# # shows a list of all todos, and lets you POST to add new tasks
# class Item(Resource):
#     def get(self):
#         return TODOS

#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
#api.add_resource(TodoList, '/todos')
api.add_resource(Item, '/item/<item_id>')


if __name__ == '__main__':
    app.run(debug=True)