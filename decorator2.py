import time

def print_name(func):
    def wrapper():
        print(f'現在正在運行 : {func.__name__}')
        func()
    return wrapper

def time_counter(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'運行共花費 : {end - start}秒')
    return wrapper

@ time_counter
@ print_name
def loop():
    for i in range(1000000):
        i += 1

loop()