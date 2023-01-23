username=str(input("enter the username:"))
password=int(input("enter the password"))
if username=="bala" and password==0000:
    print("login...")
elif username!="bala" and password==0000:
    print("invalid username")
elif username=="bala" and password!=0000:
    print("invalid password")
else:
    print("invalid user")
