import time

# The purpose of having a wrapper function is that a function decorator receives a function object to decorate, and it must return the decorated function.
def my_decorator(function):
    def wrapper(*args, **kwargs): 
        print("I'm decorating your function!")
        function(*args, **kwargs)

    return wrapper


def hello(name):
    print(f"hello {name}")


my_decorator(hello)("Milad")

# -----------------------------------------------------------------------
print("-" * 60)


def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("I'm decorating your function!")
        function(*args, **kwargs)

    return wrapper


@my_decorator
def hello(name):
    print(f"hello {name}")


hello("Milad")

# -----------------------------------------------------------------------
print("-" * 60)


def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("I'm decorating your function!")
        return function(*args, **kwargs)

    return wrapper


@my_decorator
def hello(name):
    return f"hello {name}"


print(hello("Milad"))


# -----------------------------------------------------------------------
print("-" * 60)
print("Practical Example (Logging) ...")


def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open("logfile_decorator.txt", "a+") as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"function {fname}() returned value: {value}\n")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(5, 15))


# -----------------------------------------------------------------------
print("-" * 60)
print("Practical Example (Timing) ...")


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"function {fname}() took '{after - before}' seconds to execute.")
        return value

    return wrapper


@timed
def my_func(x):
    res = 1
    for i in range(1, x):
        res *= i
    return res


my_func(10000)

print("-" * 60)
print("finished ...")
