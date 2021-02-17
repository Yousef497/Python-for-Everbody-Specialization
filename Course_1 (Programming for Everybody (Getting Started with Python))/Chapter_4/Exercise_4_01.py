def computepay(h,r):
    pay = 0
    if h <= 40:
        pay = h * r
        return pay
    else:
        h = h - 40
        pay = (40 * r) + (1.5 * r * h)
        return pay

hrs = input("Enter Hours: ")
rate = input("Enter rate per Hour: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

p = computepay(h,r)
print("Pay",p)
