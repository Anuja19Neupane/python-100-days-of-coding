# this function add can accept any number of arguments
def add(*args):  # * means this function add can accept any number of arguments
    print(args[0])
    sum=0
    for n in args:
        sum+=n
    return sum
  


print(add(3,4,5 ))


def calculate(**kwargs): #kwarg is dict 
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)


calculate(add=3,multiply=4)