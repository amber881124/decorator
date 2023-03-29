# 裝飾器(本身是一個function)
# 用function裝飾function
def decorator(func): # 接收function參數
    # 把原本的function包起來(wrap)
    def wrapper(): # 也常叫inner
        print(f'running: {func.__name__}') 
        func() # 執行被裝飾前的function
    return wrapper # 回傳被"加工"完的function

def food():
    print('水果榨汁')

# decorator(food)化身成為wrapper
food = decorator(food)
# 這個food是加工後的
food()

