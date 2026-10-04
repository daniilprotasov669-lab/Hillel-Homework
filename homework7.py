from functools import wraps

def shout(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result.upper
    return wrapper

def positive_only(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not isinstance (int, float) <= 0:
            raise ValueError
        return func(*args,**kwargs)
    return wrapper

@positive_only
def add_two(x):
    return x + 2

@shout
def add_suffix(value):
    return value + "suffix"
