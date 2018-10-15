from requests import put, get
import json
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data={'data':{'title':'mybook1','description':'mydesc1','create_at':'createbook1','create_by':'1111','priority':'1' }}
put('http://localhost:5000/notes/1', data=json.dumps(data),headers=headers)

print(get('http://localhost:5000/notes/1').json())

