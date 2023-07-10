from database import User

try:
    jina = input("enter name\n")
    arafa = input("enter email\n")
    nenosiri = input("enter your password\n")
    user.create(name = jina, email = arafa, password = nenosiri)
    print("user created successfully")

except:
    print("failed to create user")
