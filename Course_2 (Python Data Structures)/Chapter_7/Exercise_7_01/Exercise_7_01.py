fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be found: ",fname)
    quit()

inp = fhand.read()
inp = inp.upper()
inp = inp.rstrip()
print(inp)
