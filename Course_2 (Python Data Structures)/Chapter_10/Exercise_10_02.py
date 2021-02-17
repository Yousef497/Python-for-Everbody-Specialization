fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be found: ",fname)
    quit()

hcount = dict()
hlst = list()

for line in fhand:
    line.rstrip()
    if not line.startswith("From "):
        continue

    words = line.split()
    hr = words[5].split(":")
    hcount[hr[0]] = hcount.get(hr[0], 0) + 1

for k,v in hcount.items():
    hlst.append( (k,v) )

hlst.sort()
for k,v in hlst:
    print(k,v)
