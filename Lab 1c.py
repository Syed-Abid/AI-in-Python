dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
res = {**dic1, **dic2, **dic3}
print(res)

# Program to print a specified list
# after removing the 0th,4th and  5th elements.
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Tea pink']
sample_list.remove('Red')
sample_list.remove('Pink')
sample_list.remove('Yellow')
sample_list.remove('Tea pink')

print(sample_list)
