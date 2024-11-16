
def operation_decorator(func):
    def wrapper(x, y, operation):
        if operation == '+':
            return func(x, y, lambda x, y: x + y)
        elif operation == '-':
            return func(x, y, lambda x, y: x - y)
        elif operation == '*':
            return func(x, y, lambda x, y: x * y)
        elif operation == '/':
            if y != 0:
                return func(x, y, lambda x, y: x / y)
            else:
                return "Error: Division by zero"
    return wrapper

@operation_decorator
def calculate(x, y, operation_func):
    return operation_func(x, y)

result = calculate(5, 3, '+')
print(result)
