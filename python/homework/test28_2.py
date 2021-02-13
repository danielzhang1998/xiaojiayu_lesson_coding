f1 = open('/Users/zhanghanlin/Documents/OpenMe.mp3',encoding='gbk')
f2 = open('/Users/zhanghanlin/Documents/OpenMe.txt', 'x')        # 使用”x”打开更安全
f2.write(f1.read())
f2.close()
f1.close()