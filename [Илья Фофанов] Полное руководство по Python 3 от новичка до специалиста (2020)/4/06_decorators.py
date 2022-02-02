from timeit import default_timer as timer
from functools import wraps
import math
import time


def hello_world():
    print('hello world')


hello_world()

hello2 = hello_world
hello2()


def hello_world():
    def internal():
        print('hello world!')

    return internal


hello2 = hello_world()
print(hello2)
hello2()


def say_something(func):
    func()


def hello():
    print('hello !!!')


say_something(hello)


def log_decorator(func):
    def wrap():
        print(f'Coding func {func}')
        func()
        print(f"Func {func} finished its work")

    return wrap


def new_hello():
    print('new_hello')


wrapped_by_logger = log_decorator(new_hello)
wrapped_by_logger()


@log_decorator
def hello():
    print('@ hello')


hello()

print('=================================')


def measure_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()

        print(f"Function {func.__name__} took {end - start} for execution ")

    return inner


@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))


factorial(100)
