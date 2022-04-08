import requests

url = 'http://ip-api.com/json/'

ip = input('Ingresa la ip ')

r = requests.get(url + ip ).json()
print(r)