# step-1: create functions:
# Function to add two numbers 

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

  

#Step-2: user input 
print("Please select a operation:\n " \
    "1. Addition\n" \
    "2. Substraction\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Average\n"\
    "Or enter an alphabet if you want to exit the code\n") 

while True:
    try:
        select = int(input("Select a operation from 1,2,3,4,5: "))
        if select in range (1,6):
            break
        else: print("enter a number or an alphabet if you want to exit the program")
    except ValueError:
        print("the program has been terminated")
        exit()
        
    
# takes in the input numbers. If there is a no input given the program considers the default input to be 0
if select in (1, 2, 3, 4, 5):
    a = print("Enter the numbers whose operate on:")
    while True:
        try:
            number = input("enter the numbers here: ")
            if number == "":
                break # break out of the loop if no number is given
            else:
                number_list.append(float((number)))
        except ValueError:
            print("you have enterd an alphabet so the program has been terminated")
            exit()
    # Step 3: Perform the operation using match-case
    match select:
        case 1:
            print(add(number_list)) 
        case 2:
            print(minus(number_list))
        case 3:
            print(multiply(number_list))
        case 4:
            print(divid(number_list))
        case 5:
            print(average(number_list))
else:
    print("Invalid input. Please select a number between 1 and 5.")
