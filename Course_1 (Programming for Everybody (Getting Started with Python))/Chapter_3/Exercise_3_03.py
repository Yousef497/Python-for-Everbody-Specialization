sco = input("Enter Score: ")
try:
    score = float(sco)
except:
    print("Error, please enter a numeric value.")

if (score < 0.0) or (score > 1.0):
    print("Error, Score is out of range.")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
