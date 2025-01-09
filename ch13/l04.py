
def factorial(num):
    for i in range(num - 1, 0, -1):
        num *= i
    return num if num != 0 else 1

def debug_factorial(num):
    operation = ""
    for i in range(num - 1, 0, -1):
        operation += f"{num} * {i}" if operation == "" else f" * {i}"
        print(operation)
        num *= i
    return num if num != 0 else 1

print(debug_factorial(10))