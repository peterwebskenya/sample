def calculate_bmi():
    weight = float(input("enter weight"))
    height = float(input("enter height"))

    bmi = weight / (height * height)
    print(f"your bmi is{bmi}kg/m2")
calculate_bmi()

