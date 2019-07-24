class Log(object):
    def __init__(self,n):
        self.buffer=[None]*n
        self.curr_ind=0

    def record(self,id):
        self.buffer[self.curr_ind]=id
        self.curr_ind+=1
        if self.curr_ind == len(self.buffer):
            self.curr_ind=0

    def get_last(self,n):
        start_ind=self.curr_ind-n
        print(start_ind)
        if start_ind < 0:
            return (self.buffer[start_ind:]+self.buffer[:self.curr_ind])
        else:
            return self.buffer[start_ind:self.curr_ind]


log=Log(10)
for id in range(25):
    log.record(id)

print(log.curr_ind)
print(log.get_last(1))
print(log.get_last(0))
print(log.get_last(8))
