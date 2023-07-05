i = int(input("enter number"))
v = int(input("enter second number"))
for x in range (i,v + 1):
    if x % 3 ==0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    elif(x % 3 == 0) and (x % 5 == 0):
        print("fizzbuzz")
    else:
        print(x)
