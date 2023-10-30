# Write a python program to accept the data for a number
# of
# cities from the keyboard and store the data in a file in the order in which they’re entered.
def getData():
    city = input("Enter city name:- ")
    population = int(input("Enter city population:- "))
    mayor = input("Enter city mayor:- ")
    return {
        "city": city,
        "population": population,
        "mayor": mayor
    }

def writeData(data):
    file = open("cityData.csv", "a")
    file.write(f'{data["city"]},{data["population"]},{data["mayor"]}\n')
    file.close()

numberOfCities = int(input("Enter number of cities you want to store data of:- "))

for i in range(numberOfCities):
    data = getData()
    writeData(data)

# Write a python program to create a data file student.txt and append the message “Now we are
# AI students”s
#f = open("student.txt","a")
#f.write("Now we are AI students!")
#f.close()
#f = open("student.txt","r")
#f.read()