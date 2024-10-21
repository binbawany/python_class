
def calculator(operation,a,b):
    if operation == 'add':
        return a+b
    elif operation == 'subtract':
        return a-b
    elif operation == 'multiply':
        return a*b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by Zero"
    else:
        return "Invalid Operation"

print(calculator("multiply", 2j, 0))
    