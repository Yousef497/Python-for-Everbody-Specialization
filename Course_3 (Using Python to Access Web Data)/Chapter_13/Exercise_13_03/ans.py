import urllib.request, urllib.parse, urllib.error
import json
adr= 'http://py4e-data.dr-chuck.net/json?'
while True:
    loca= input('Enter Location: ')
    if len(loca)<1:break

    url=adr + urllib.parse.urlencode({"address": loca})
    print('Retrieving', url)
    fha=urllib.request.urlopen(url)
    data=fha.read().decode()
    print('Retrieved', len(data))

    jsdata=json.loads(str(data))
    placeid= jsdata['results'][0]['place_id']
    print('The Place ID is: ', placeid)
