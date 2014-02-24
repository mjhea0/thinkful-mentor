import requests

def test():
    url = 'http://httpbin.org/post'
    data = {'a': 10, 'b': [{'c': True, 'd': False}, None]}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    return json.dumps(r.status_code, indent=4)


print test()

    # r.status_code
    # r.elapsed
    # r.url
    # r.json()
