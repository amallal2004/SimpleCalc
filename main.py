import os
from art import logo


# Function to perform addition
def add(n1, n2):
    return n1 + n2


# Function to perform subtraction
def subtract(n1, n2):
    return n1 - n2


# Function to perform multiplication
def multiply(n1, n2):
    return n1 * n2


# Function to perform division
def divide(n1, n2):
    return n1 / n2


# Dictionary mapping operation symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Main calculator function
def calculator():
    print(logo)

    # Get the first number from the user
    num1 = float(input("What's the first number?: "))

    # Display the available operation symbols
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        # Get the operation symbol from the user
        operation_symbol = input("Pick an operation: ")

        # Get the second number from the user
        num2 = float(input("What's the next number?: "))

        # Perform the calculation based on the selected operation symbol
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # Display the result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Check if the user wants to continue with the answer or start a new calculation
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            # Clear the terminal screen and start a new calculation
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()


# Start the calculator program
calculator()
