from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
numbers = list()

for span in spans:
    numbers.append(int(span.string))

print(sum(numbers))
