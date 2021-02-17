import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input("Enter location: ")
url = "http://py4e-data.dr-chuck.net/json?"
address = urllib.parse.urlencode({'address': location, 'key': 42})
target = url + address
print("Retrieving", target)
uhand = urllib.request.urlopen(target)
data = uhand.read()
print("Retrieved", len(data), "characters")
parsed = json.loads((data))

#print(parsed)

print ("Place id", parsed["results"][0]["place_id"])
