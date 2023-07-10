#create another table student
# have the following
 #    phone
  #   age
   #  gender
    # studentcode
     #_____student created successfully



try:
    simu = input("enter phone_number\n")
    umri = input("enter age\n")
    jinsia = input("enter gender\n")
    nambari_sajiri = input("enter studentcode\n")
    student.create(phone_number = simu, age = umri, gender = jinsia)
    print("student created successfully")

except:
    print("failed to create student")
