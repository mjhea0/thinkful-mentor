from flask import Flask
import requests
import json

app = Flask(__name__)



@app.route('/')
def test():
    url = 'http://httpbin.org/post'
    data = {'a': 10, 'b': [{'c': True, 'd': False}, None]}
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    return json.dumps(r.json(), indent=4)

if __name__ == '__main__':
    app.run(debug=True)
