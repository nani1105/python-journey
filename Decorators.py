import time

# Basic decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before the function runs")
        result = func(*args, **kwargs)
        print("after the function runs")
        return result
    return wrapper

@my_decorator
def greet():
    print("Hello Giri")

@my_decorator
def add(a, b):
    return a + b

greet()
print(add(3, 4))

# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("function done")

slow_function()