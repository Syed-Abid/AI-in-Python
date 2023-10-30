# Program of while loop
#n = 4
#while n <= 56:  # when n > 0 the loop never ends
#    n += 1
#    print(n)

# Program to create a list of countries
#clist = ['Canada', 'USA', 'Mexico', 'Australia']
#cset = set(clist)
#print(sorted(cset))

# Program to create a list of countries using while loop
clist = ['Canada', 'USA', 'Mexico', 'Australia']
i = 0
cset = set()
while i < len(clist):
    cset.add(clist[i])
    i += 1
print(cset)


