import time

total_time = 0

def timeslong(func):    # 传入 f() 函数
    def call():
        global total_time
        start = time.perf_counter() # f() 开始前计时
        #print("It's time starting ! ")
        func()  # 在此处调用 f()
        #print("It's time ending ! ")
        end = time.perf_counter()   # f() 结束后停止计时
        total_time += (end - start)
    return call

@timeslong
def test():
    text = "I love FishC.com!"
    char = 'o'
    if char in text:
            pass

for i in range(1000000):
    test()
    #print(test())
print(total_time)