import json
from urllib.request import urlopen

resp = urlopen('https://ipinfo.io/json')
data = json.load(resp)
ip = data['ip']
print(data)
