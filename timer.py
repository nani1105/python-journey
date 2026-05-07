import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} took {end-start:.4f}seconds")
        return result
    return wrapper
@timer
def add(a,b):
    return a+b

@timer
def slowtimer():
    time.sleep(1)
    print("done")
print(add(3,4))
slowtimer()