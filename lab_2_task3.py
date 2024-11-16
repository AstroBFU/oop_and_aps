

import math
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}")

        result = func(*args, **kwargs)

        print(f'{func.__name__} returned: {result}')

        return result

    return wrapper

@debug
def sq(x, y):
    return math.sqrt(x * y)

result = sq(3, 3)
