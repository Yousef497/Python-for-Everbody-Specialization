fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be found: ",fname)
    quit()

lst = list()
for line in fhand:
    line.rstrip()

    for i in line.split():
        if not i in lst:
            lst.append(i)

lst.sort()
print(lst)
