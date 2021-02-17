import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tot = 0
number = 0

url = input("Enter location: ")
print("Retrieving:",url)
uhand = urllib.request.urlopen(url)
data = uhand.read()
print("Retrieved", len(data), "characters")

info = json.loads(data)
info = info['comments']

for item in info:
    number = number + 1
    tot = tot + int(item["count"])

print("Count:", number)
print("Sum:", tot)
