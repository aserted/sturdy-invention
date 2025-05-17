# sturdy-invention
First time creating a simple calculator
<br>
using function, try/except, match etc
<br>
explanantion:
<br>
This part defines the function to do addition, subtraction, average, multiplication and division <br>
the functions have the parameter numbers
<br>
number_list = []
def add(numbers):
     return sum(numbers) 

# Function to substract two numbers 
def minus(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Function to multiply two numbers 
def multiply(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result *= num
    return result

# Function to divide two numbers 
def divid(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

# Function to average two numbers 
def average(numbers):
    return sum(numbers)/len(number_list)
