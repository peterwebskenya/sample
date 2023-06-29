weight = float(input("enter you mass in kilos"))
height = float(input("enter your height"))

bmi = weight / (height*height)
if bmi <= 18:
    print("underweight")
elif bmi <= 29.0:
    print("normal weight")
elif bmi <= 34.0:
    print("overweight")
else:
    print("obese")

    print("Your bmi is", bmi, "kg/m2")