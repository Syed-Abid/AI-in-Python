# Program to find the efficiency of the worker
workhours = float(input("Enter the number of hours worked: "))
if workhours >= 2.0 and workhours < 3.0:
    print("Worker is highly efficient!")
elif workhours > 3.0 and workhours <=4.0:
    print("You should improve your speed!")
elif workhours > 4.0 and workhours <=5.0:
    print("You need training!")
elif workhours > 5.0:
    print("You have to leave the company!")
else:
    print("Try again!")
