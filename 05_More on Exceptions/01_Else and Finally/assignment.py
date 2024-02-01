#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter the second number"))
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    value = number1/number2
    print('The answer is', value) 
   
except ZeroDivisionError:
    print("This answer is not possible")
else:
    print("no division errors are detected")

finally:
    print("division taken care of")
