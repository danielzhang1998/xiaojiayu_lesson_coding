import time
 
def timeslong(func):    # 传入 f() 函数
    def call():
        start = time.perf_counter() # f() 开始前计时
        print("It's time starting ! ")
        func()  # 在此处调用 f()
        print("It's time ending ! ")
        end = time.perf_counter()   # f() 结束后停止计时
        return "It's used : %s ." % (end - start)
    return call

@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

print(f())