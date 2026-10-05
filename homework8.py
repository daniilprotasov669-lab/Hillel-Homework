def log_args(func):
    def wrapper(*args):
        print(args)
        return func
    return wrapper



def repeat(times):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(times):
                func(*args,**kwargs)
            return wrapper
        return decorator

@repeat(3)
def message():
    print("hello")



words = ["apple", "cat", "banana", "dog"]

for word in words:
    if (length := len(word)) > 4:
        print(word, length)



def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "start"

for number in countdown(5):
    print(number)