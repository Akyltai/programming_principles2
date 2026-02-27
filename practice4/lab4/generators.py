#1
def give_sequence(end):
    cnt = 1
    while cnt<=end:
        yield cnt
        cnt+=1
x = give_sequence(59)
for i in x:
    print(i)
#2
create_square_for_nums = (x*x for x in range(1,5))
for i in create_square_for_nums:
    print(i)
#3
class Fibonachi_nums():
    def __init__(self,end):
        self.end = end
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a < self.end:
            current = self.a
            self.a,self.b = self.b,self.a + self.b
            return current
        else:
            raise StopIteration
fibon = Fibonachi_nums(900)
for i in fibon:
    print(i)
#4
def even_gen():
    n = 0
    while True:
        yield n
        n+=2
gen = even_gen()
for _ in range(9):
    print(next(gen))
#5
def filter_long_words(text, length):
    for word in text.split():
        if len(word) > length:
            yield word
gen = filter_long_words("I honestly very want GPA 4.0000",3)
for i in gen:
    print(i,end=" ")