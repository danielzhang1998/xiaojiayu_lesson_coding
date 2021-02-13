import time as t

class MyTimer():

    def __init__(self):
        self.unit = [' year',' month',' day',' hour',' minute',' second']
        self.prompt = 'does not start yet!'
        self.lasted = []
        self.start = 0
        self.stop = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__
    
    # start count the time
    def begin(self):
        self.start = t.localtime()
        print('start count the time')

    # stop count the time
    def end(self):
        self.stop = t.localtime()
        print('stop count the time')
        self._calc()

    # count the running time
    def _calc(self):
        self.lasted = []
        self.prompt = 'total running time: '
        for each in range(6):
            self.lasted.append(self.stop[each] - self.start[each])
            if self.lasted[each]:
                self.prompt += (str(self.lasted[each]) + self.unit[each])

