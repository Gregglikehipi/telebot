import requests

def api_get(id):
    r = requests.get(f'http://127.0.0.1:8000/get/{id}')
    response = json.loads(r.text)
    return response

def api_add(id):
    r = requests.post(f'http://127.0.0.1:8000/add/{id}')
    response = json.loads(r.text)
    return response

def api_get_all():
    r = requests.get('http://127.0.0.1:8000/get_all/')
    response = json.loads(r.text)
    return response

def api_delete(id):
    r = requests.delete(f'http://127.0.0.1:8000/delete/{id}')
    return response

def api_priceHistory(id):
    r = requests.get(f'http://127.0.0.1:8000/historyPrice/{id}')
    response = json.loads(r.text)
    return response

def api_countGroup(id):
    r = requests.get(f'http://127.0.0.1:8000/countGroup/{id}')
    response = json.loads(r.text)
    return response

def api_countAll(id):
    r = requests.get(f'http://127.0.0.1:8000/countAll')
    response = json.loads(r.text)
    return response

def api_average(id):
    r = requests.get(f'http://127.0.0.1:8000/comparePrice/{id}')
    response = json.loads(r.text)
    return response
