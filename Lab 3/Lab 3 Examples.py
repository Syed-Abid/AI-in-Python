# Example 1
x = lambda a : a + 10
print(x(5))

# Example 2
x = lambda a, b : a * b
print(x(5, 6))

# Example 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Example 4
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Example 5
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars)

# Example 6
x = len(cars)
print(x)

# Example 7
for x in cars:
 print(x)

# Example 8
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# Example 9
f = open("demofile2.txt", "r")
print(f.read())

# Example 10
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# Example 11
f = open("demofile3.txt", "r")
print(f.read())

