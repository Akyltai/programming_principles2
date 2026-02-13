#1
def say_hello(name):
    print(f"Hello {name}!")
say_hello("Karina")
# 2
def check_number(num):
    if num%2 == 0:
        print("It's odd number")
    else:
        print("even number")
check_number(4)
# 3
def yo_or_yeah(word):
    if len(word) > 5:
        print("Yo!")
    else:
        print("Yeah!")
yo_or_yeah("Hellou")
#4
def calculator(num1,num2,oper):
    if oper == '+':
        return num1+num2
    if oper == '-':
        return num1-num2
    if oper == '*':
        return num1*num2
    if oper == '//':
        return num1//num2
    else:
        print("Error,try again")
print(calculator(7,8,'*'))
#5
def are_u_ok(response):
    match response:
        case 'yes':
            print("Are you sure? Okey")
        case 'no':
            print("Why? What happened?")
        case _:
            print("Wtf,what you mean?")
are_u_ok('yes')