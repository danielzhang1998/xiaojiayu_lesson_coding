try:
    
    f = open('我是一个不存在的文件.txt','w')
    print(f.write('I am an exists file!'))
    sum = 1 + '1'
    f.close()
except (OSError,TypeError):
    print('error!')
finally:
    f.close()


