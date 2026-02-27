class Iter():
    def __init__(self,st):
        self.st = st
        self.a = len(self.st)
        self.x = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.a > 0:
            self.x = self.a -1 
            self.a-=1
            return self.st[self.x]
        else:
            raise StopIteration
n = input()
it = Iter(n)
for x in it:
    print(x,end="")