#1
score_determinator={
    'discreate math':lambda a,b:a*b,
    'linear algebra':lambda a,b:a**b
}
print(score_determinator['discreate math'](2,15))
#2
sum = (lambda x,y,z:x+y+z)
print(sum(34,45,56))
#3
def lam_func(a):
    return lambda b:a+b
helper_func = lam_func(5)
print(helper_func(4))
#4
s = (lambda x,y: x**y)
print(s(2,5))
#5
def calculator(a,b):
    return lambda c:(a+b)*c
help_lam_func = calculator(2,3)
print(help_lam_func(5))