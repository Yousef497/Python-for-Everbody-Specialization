fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be found:", fname)
    quit()

count = 0
for line in fhand:
    line.rstrip()

    if line.startswith("From "):

        if len(line) < 1:
            continue

        count = count + 1
        mail = line.split()
        print(mail[1])


print("There were", count, "lines in the file with From as the first word")
