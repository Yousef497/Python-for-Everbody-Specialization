largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        ival = float(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = ival
    elif ival > largest:
        largest = ival
    elif smallest is None:
        smallest = ival
    elif ival < smallest:
        smallest = ival

def done(largest, smallest):
    print("Maximum is",int(largest))
    print("Minimum is",int(smallest))

done(largest,smallest)
