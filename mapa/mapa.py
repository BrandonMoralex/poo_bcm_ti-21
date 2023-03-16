import requests

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
}
call = requests.get('https://api.openrouteservice.org/v2/directions/driving-hgv?api_key=5b3ce3597851110001cf62482d9f9ebc8bb04cc3b54024f5cef354da&start=-98.4051257,20.0755977&end=-98.3895071,20.0761642', headers=headers)

print(call.status_code, call.reason)
print(call.text)