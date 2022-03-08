""" geberator => 1-functions 2-expression(comprehension)
yeild show that a function was a generator

Lazy evaluation: It will not be called until it has to

"""

import sys
from datetime import datetime as time

# custom generator ------------------------------------------------
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last**2
        self.last += 1
        return rv


# speed test ------------------------------------------------------


t1 = time.now()


def generator_iter():
    for i in range(100000):
        yield i**2


g = generator_iter()
while True:
    try:
        print(next(g))
    except:
        break

t2 = time.now()


def loop_iter():
    for i in range(100000):
        print(i**2)


loop_iter()


print("generator time : ", t2 - t1)
print("loop time : ", time.now() - t2)

# function --------------------------------------------------------
def my_function(n):
    while n > 0:
        n -= 1
    return n


def my_generator(n):
    while n > 0:
        yield n
        n -= 1


values = my_generator(5)
values2 = my_function(5)

for i in values:
    print(i)


print("*" * 60)


# expression --------------------------------------------------------
even_generator = (s for s in range(1, 100) if s % 2 == 0)
even_list = [s for s in range(1, 100) if s % 2 == 0]


print("size of generator: ", sys.getsizeof(even_generator))
print("size of list: ", sys.getsizeof(even_list))
