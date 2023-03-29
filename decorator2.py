import time

def time_counter(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__}運行共花費 : {end - start}秒')
    return wrapper

def loop():
    for i in range(1000000):
        i += 1

loop = time_counter(loop)
loop()