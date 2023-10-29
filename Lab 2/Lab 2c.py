# Program to check the password
password = 'abc$123'
pass1 = 'ABC$123'
userinput = str(input("Enter the password: "))
if userinput == password or pass1:
    print("Welcome!")
else:
    print("I don't know you!")
