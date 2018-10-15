from requests import put, get
import json
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# data={'name':'mybook1','quantity':20 }
# put('http://localhost:5000/items/1', data=json.dumps(data),headers=headers)

# print(get('http://localhost:5000/items/1').json())

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data1={'data':'Meeting at 10Oct18 10am'}
data2={'data':'Class at 12Nov18 9am'}

put('http://localhost:5000/todo1', data=data1).json()
put('http://localhost:5000/todo2', data=data2).json()
print(get('http://localhost:5000/todo1').json())
print(get('http://localhost:5000/todo2').json())
