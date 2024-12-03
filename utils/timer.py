import time


def timer(iterations=1):
    """
    Print the duration of an input function
    :param int iterations: how many times to loop the function
    :return func:
    """
    def functionDecorator(func):
        def wrapper(*args, **kwargs):
            result = None
            t1 = time.time()
            for i in range(iterations):
                result = func(*args, **kwargs)
            t2 = time.time()
            print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
            return result
        return wrapper

    return functionDecorator
