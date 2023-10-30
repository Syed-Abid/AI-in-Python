# a Python program to square and cube every number in a given list of integers using Lambda.
#num_list = [2,4,6,8,10,12,14]
#print('Given List:',num_list)
#square = print(list(map(lambda x : x ** 2,num_list)))
#cube = print(list(map(lambda  x: x ** 3,num_list)))

# a Python program to find if a given string starts with a given character using Lambda.
#start_with = lambda x: True if x.startswith('P') else False
#print(start_with('Program'))
#start_with = lambda x: True if x.startswith('P') else False
#print(start_with('Lab'))

# a Python program to extract year, month, date and time using Lambda.
import datetime
current = datetime.datetime.now()
print(current)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(current))
print(month(current))
print(day(current))
print(t(current))
