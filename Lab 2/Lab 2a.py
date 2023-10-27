# Program that prints the volume of boxs and give them labels
# according to their size
height = int(input("Enter the height: "))
width = int(input("Enter the width: "))
depth = int(input("Enter the depth: "))
volume = height * width * depth
print(volume)
if volume >= 1 and volume <= 10:
    print("Extra Small")
elif volume >= 11 and volume <= 25:
    print("Small")
elif volume >= 26 and volume <= 75:
    print("Medium")
elif volume >= 76 and volume <= 100:
    print("Large")
elif volume >= 101 and volume <= 250:
    print("Extra Large")
elif volume >= 251:
    print("Extra-Extra Large")
else:
    print("There is an error")
