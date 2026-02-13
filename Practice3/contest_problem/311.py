class Pair:
    def __init__(self,a1,b1,a2,b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
    def show_sum(self):
        print(f'Result: {self.a1+self.a2} {self.b1+self.b2}')
data = list(map(int,input().split()))
fir = data[0]
sec = data[1]
fir2 = data[2]
sec2 = data[3]
p = Pair(fir,sec,fir2,sec2)
p.show_sum()
    