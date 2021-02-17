import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tot = 0

url = input("Enter location: ")

print("Retrieving",url)
uhand = urllib.request.urlopen(url)
data = uhand.read()
print("Retrieved", len(data), "characters")
#print(data.decode())
tree = ET.fromstring(data)
lst = tree.findall('.//count')
count = len(lst)
#print(lst)


for val in lst:
    tot = tot + int(val.text)

print("Count:", len(lst))
print("Sum:", tot)
