number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter another number"))
except ValueError:
    print("integer was not given")

try:
    value = number1/number2
    print('The answer is', value) 
except ZeroDivisionError:
    print("the division is not possible")

    
