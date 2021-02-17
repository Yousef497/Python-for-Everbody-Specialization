hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")
h = float(hrs)
r = float(rate)
pay = 0
if h <= 40:
    pay = h * r
    print(pay)
else:
    h = h - 40
    pay = (40 * r) + (1.5 * r * h)
    print(pay)
