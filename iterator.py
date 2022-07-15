class RemoteControl():
    def __init__(self):
        self.channel=("HBO", "ABC", "ID", "HistoryTV18","Sony","NatGeo")
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index==len(self.channel):
            raise StopIteration
        return self.channel[self.index]

c=RemoteControl()
itr=iter(c)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
