# Simple Math Operations Program
# Handles Addition, Subtraction, Multiplication, Division, Average, Modulo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def average(a, b):
    return (a + b) / 2

def modulo(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Cannot modulo by zero!"

print("Welcome to Simple Math Operations Program!")
print("Options: add, sub, multiply, divide, average, modulo")

operation = input("Enter operation: ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        print("Result:", add(num1, num2))
    elif operation == "sub":
        print("Result:", subtract(num1, num2))
    elif operation == "multiply":
        print("Result:", multiply(num1, num2))
    elif operation == "divide":
        print("Result:", divide(num1, num2))
    elif operation == "average":
        print("Result:", average(num1, num2))
    elif operation == "modulo":
        print("Result:", modulo(num1, num2))
    else:
        print("Error: Invalid operation!")

except ValueError:
    print("Error: Please enter valid numbers!")
