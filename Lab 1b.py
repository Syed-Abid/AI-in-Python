num_1 = [2, 4, 6, 8]
num = [1, 2, 3, 4, 5, 6]
print(num)
num.append(7)
print(num)
print(num.count(2))
num.extend(num_1)
print(num)
print(num.index(2))
num.insert(5, 9)
print(num)
num.remove(3)
print(num)
num.reverse()
print(num)
num.sort()
print(num)


def func1(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr


print(func1(['abc', 'xyz', 'aba', '1221']))
