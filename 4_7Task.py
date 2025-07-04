#Basic Input with Integer Conversion
#Take two numbers as input from the user, convert them to integers, and print their sum.
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
total=a+b 
print("The sum of two numbers is: ", sum) 
#Multiple Inputs with Space Separation
#Take two floating-point numbers as input in a single line separated by space and print their product.
a, b = map(float, input("Enter two floating-point numbers separated by space: ").split())
product = a * b
print("The product of the two numbers is:", product)
#Expression Evaluation with eval()
#Take a mathematical expression from the user as input and print the evaluated result.
# Take mathematical expression as input
expression = input("Enter a mathematical expression: ")
result = eval(expression)
print("The result is:", result)
#List Input using eval()
#Take a list as input using eval() and print the sum of its elements.
lst = eval(input("Enter a list of numbers: "))
print("The sum of the list elements is:", sum(lst))
#Boolean Type Conversion
#Take an input from the user, convert it to boolean, and print the result
u = input("Enter a value: ")
b = bool(u)
print("Boolean value is:", b)
#String to Float Conversion
#Take a floating-point number as string input, convert it to float, and print its square.
num_str = input("Enter a floating-point number: ")
num = float(num_str)
square = num ** 2
print("The square of the number is:", square)
#Dictionary Input using eval()
#Take a dictionary as input using eval() and print its keys and values separately.
d = eval(input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): "))
print("Keys:", d.keys())
print("Values:", d.values())
#List of Integers from Space Separated Input
#Take a list of integers as input in a single line separated by space and print the maximum and minimum values.
d = eval(input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): "))
print("Keys:", d.keys())
print("Values:", d.values())
#Mixed Type Literal Input with eval()
#Take any Python literal as input (string, list, tuple, int, etc.) using eval() and print its type.
value = eval(input("Enter any Python literal (e.g., 10, 'hello', [1,2], (3,4)): "))
print("The type of the input is:", type(value))
#Combined Type Conversion
#Take two inputs, convert the first to integer and second to float, then print their sum.
int_input = int(input("Enter an integer: "))
float_input = float(input("Enter a floating-point number: "))
total = int_input + float_input
print("The sum is:", total)

