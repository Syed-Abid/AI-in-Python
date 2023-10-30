# Print square root of a negative or positive numbers
a = int(input("Enter a number and I'll get it's square root: "))
if a > 0:
    print("The number you entered is greater ")
    root = a ** (1 / 2)
    print("The square root of %d is %f" % (a, root))
if a <= 0:
    print("I can't calculate the square root of a negative number!")
print("Thanks for the input!")

# Writing conditional statements to print value of 0 to 1
# and 1 to 0 and numbers in between
a = int(input())
if a == 1:
    a = 0
if a == 0:
    a = 1
if a > 2 or a < 0:
    print("You have entered number between")
print(a)

# Another Example
a = int(input("Enter a number between 10-20: "))
if a >= 10 and a <= 20:
    print("The condition has been met.")
else:
    print("You did it wrong.")

# Another Example
a = int(input("Enter a number between 10-20 or 30-40: "))
if (a >= 10 and a <= 20) or (a >= 30 and a <= 40):
    print("The condition has been met.")
else:
    print("You did it wrong.")

# Print Karachi Pakistan 100 times in separate line
i = 1
while(i <=100 ):
    print("Karachi Pakistan")
    i += 1
# OR
i = 100
while(i >= 1):
    print("Karachi Pakistan")
    i -= 1

# Counting positive and negative numbers
pcount = 0
ncount = 0
count = int(input("how many numbers you want? "))
i = 1
while(i <= count):
    num = int(input("Enter number: "))
    if(num >= 0):
        pcount += 1
    else:
        ncount += 1
    i += 1
print("positive: ", pcount)
print("negative: ", ncount)

# Fixed a letter from a to e and then ask the user to
# guess that letter until correct letter entered
value = "c"
uservalue = input("guess a number from a to e:    ")
while(uservalue != value):
    print("Incorrect")
    uservalue = input("guess a number from a to e:  ")
print("Welcome User!")
