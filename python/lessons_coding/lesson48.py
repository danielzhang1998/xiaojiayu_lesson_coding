class Countlist:
    def __init__(self,*args):
        '''
        将 args 里面的所有数字放入到 values 列表里
        假设有1，2，3，4，5，6
        name将得到 [1，2，3，4，5，6]
        '''
        self.values = [x for x in args]
        '''
        fromkeys()为新建一个字典
        长度为 values 列表的长度
        以 列表中每一个元素的下标作为 key，访问次数作为 value
        初始的 value 均设置为 0
        '''
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key] += 1
        return self.values[key]
