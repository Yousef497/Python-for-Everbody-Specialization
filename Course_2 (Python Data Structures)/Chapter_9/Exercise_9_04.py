fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be found:",fname)
    quit()

counts = dict()
for line in fhand:
    line.rstrip()

    if line.startswith("From "):
        if len(line) < 1:
            continue

        words = line.split()
        counts[words[1]] = counts.get(words[1],0) + 1

bigcount = None
mail = None
for word,count in counts.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        mail = word

print(mail, bigcount)
