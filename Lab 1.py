def swap(a, b, c, d):
    # Step1 (Swapping a and d)
    a = a + d
    d = a - d
    a = a - d
    # Step2 (Swapping b and c)
    b = b + c
    c = b - c
    b = b - c

    print("Values after swapping:")
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)


a1 = int(input("Enter a number:"))
b1 = int(input("Enter a number:"))
c1 = int(input("Enter a number:"))
d1 = int(input("Enter a number:"))
swap(a1, b1, c1, d1)
