# To convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))
# To convert Celsius to Fahrenheit
celsius1 = float(input("Enter temperature in celsius: "))
fahrenheit1 = ((celsius1 * 9/5) + 32)
print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius1, fahrenheit1))
