from requests import put, get
import json
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# data={'name':'mybook1','quantity':20 }
# put('http://localhost:5000/items/1', data=json.dumps(data),headers=headers)

# print(get('http://localhost:5000/items/1').json())

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data1={'name':'mybook1','qty':100}
data2={'name':'mybook2','qty':200}

put('http://localhost:5000/item1', data=data1).json()
put('http://localhost:5000/item2', data=data2).json()
print(get('http://localhost:5000/item1').json())
print(get('http://localhost:5000/item2').json())
