def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned value: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

result = add(3, 4)
