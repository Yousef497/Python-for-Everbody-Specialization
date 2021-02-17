fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be found: ",fname)
    quit()

count = 0
tot = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    space = line.find(" ")
    substring = line[space:]
    substring = float(substring)
    tot = tot + substring
    count = count + 1

print("Average spam confidence:", (tot / count))
