celsius_temperatures=[100,35,78,56]
fahrenheit_temperatures=[90,104,308,456]

def celsiusToFahrenheit(temp):
    return temp*(9/5)+32
def fahrenheitToCelsius(temp):
    return (temp-32)*5/9

print(list(map(celsiusToFahrenheit,celsius_temperatures)))
print(list(map(fahrenheitToCelsius,fahrenheit_temperatures)))

'''Acheiving the above functions via lamba'''

print(list(map(lambda t:t*(9/5)+32,celsius_temperatures)))
print(list(map(lambda t:(t-32)*5/9,fahrenheit_temperatures)))