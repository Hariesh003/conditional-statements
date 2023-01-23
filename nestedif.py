Nationality=str(input("enter Nationality:"))
age=int(input("age:"))
if Nationality=="indian":
    if age>=18:
        print("eligible for voting")
    else:
        print("unger age")
else:
    print("not eligible for voting")
