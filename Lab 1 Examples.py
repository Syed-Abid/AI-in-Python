print(1 + 1)
print(2 * 3)
print(1 == 0)
print(not(1 == 0))
print((2 == 2) and (2 == 3))
print('HELP'.lower())
print('artificial'.upper())
s = 'hello world'
print(s.upper())
print(len(s.upper()))
num = 8.0
num += 2.5
print(num)
fruits = ['apple', 'orange', 'pear', 'banana']
print(fruits[0])
otherfruits = ['kiwi', 'strawberry']
print(fruits + otherfruits)
print(fruits[-2])
print(fruits.pop())
print(fruits.append('grapefruit'))
print(fruits[:2])
print(fruits[1:])
print(fruits[0:3])
listoflist = [['a', 'b', 'c'], [1, 2, 3], ['one', 'two', 'three']]
print(listoflist[1][2])
print(listoflist[1].pop())
pair = (3, 5)
print(pair[0])
x, y = pair
print(y)
setofshapes = {'rectangle', 'square', 'triangle', 'circle'}
setofshapes.add('polygon')
print('circle' in setofshapes)
print('polygon' in setofshapes)
favoriteshapes = {'circle', 'triangle'}
setoffavoriteshapes = setofshapes - favoriteshapes
print(setoffavoriteshapes)
studentid = {'knuth': 56.0, 'parth': 45.0, 'elvish': 35.0}
print(studentid['elvish'])
print(studentid.keys())
print(studentid.values())
print(studentid.items())
fruits = ['apple', 'banana', 'pear', 'peach']
for fruits in fruits:
    print(fruits + ' for sale')
fruitprices = {'apples': 2.00, 'oranges': 1.75, 'pears': 1.50}
for fruits, price in fruitprices.items():
    if price < 2.00:
        print('%s cost %f a pound' % (fruits, price))
    else:
        print(fruits + ' are too expensive')
print(list(map(lambda x: x * x, [1, 2, 3])))
print(list(filter(lambda x:x > 3, [1, 2, 3, 4, 5, 4, 3, 2, 1])))
num = [1, 2, 3, 4, 5, 6]
plusonenum = [x + 1 for x in num ]
oddnums = [x for x in num if x % 2 == 1]
print(plusonenum)
print(oddnums)
