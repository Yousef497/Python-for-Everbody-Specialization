import re

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be found:",fname)
    quit()

sum = 0

for line in fhand:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        number = int(number)
        sum = sum + number

print(sum)
