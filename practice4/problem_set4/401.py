class Power_of_two_for_n_integer():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
myclass = Power_of_two_for_n_integer()
myiter = iter(myclass)
for x in myiter:
    print(x)
