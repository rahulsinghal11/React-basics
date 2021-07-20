import requests
import json
data = {
  "password": "test",
  "username": "test"
}
URL = 'https://order-pizza-api.herokuapp.com/api/auth'
r = requests.post(url = URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print(r.text)

