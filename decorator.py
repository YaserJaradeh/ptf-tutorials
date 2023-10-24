# For this file to work you need to install undecorated package
# pip install undecorated

from typing import Callable
import time
from undecorated import undecorated


def log_args_to_file(filename: str = "log.txt"):
    """
    A decorator to log the arguments of a function to a file
    :param filename: the name of the file to log to
    :return: the wrapper function which contains the actual decorator
    """
    def decorator(func: Callable):
        """
        The actual decorator
        :param func: the function to decorate
        :return: the wrapper function which is the actual decorator
        """
        def wrapper(*args, **kwargs):
            """
            The wrapper function
            :param args: positional arguments
            :param kwargs: keyword arguments
            :return: the result of the function
            """
            with open(filename, "a") as f:
                f.write(f"Arguments: {args}, {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def benchmark(func: Callable):
    """
    A decorator to benchmark (time-wise) a function
    :param func: the function to decorate
    :return: the wrapper function which is the actual decorator
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
        return result

    return wrapper


def log_caller(func: Callable):
    """
    A decorator to log the caller of a function
    Also undecorate the function to get the original name
    :param func: the function to decorate
    :return: the wrapper function which is the actual decorator
    """
    def wrapper(*args, **kwargs):
        print(f"Function {undecorated(func).__name__} is called")
        return func(*args, **kwargs)

    return wrapper


@log_caller
@benchmark
@log_args_to_file("ptf.txt")
def get_content(x: int, y: str):
    """
    Our main function that we want to decorate.
    This is a function that simulates a long-running task
    :param x: dummy int parameter
    :param y: dummy str parameter
    """
    for i in range(2):
        time.sleep(0.1)
    return "heyyyy"


def time_it(func: Callable):
    """
    A simple function to time a function.
    This is a starting point to show the need for decorators
    :param func: the function to time
    :return: Nothing
    """
    start = time.time()
    print(func())
    end = time.time()
    print(f"Time taken: {end - start}")


if __name__ == '__main__':
    # Simple call of the function
    get_content(1, y="a")
    # To simulate the need for a decorator, you can call the undecorated function like this
    print(benchmark(log_caller(get_content))(1, "a"))
