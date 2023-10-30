# Program that includes all features
def sum_generator():
    summ = 0
    res = 0
    a = input("Enter 1 to proceed, 0 to exit:")
    if a == 1:
        for x in range(10):
            summ = summ + 2
        print(summ)
    else:
        i = 1
        while i <= 10:
            res = res + 3
            print(res)
            i = i + 1


sum_generator()
