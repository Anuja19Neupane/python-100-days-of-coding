a = 2  # integer
a = "5"
b = "apple"  # string
c = 2.3  # float
d = [1, 2, 3]  # list
e = {"name": "Anuja", "class": 15}
# dictonary
len(d)
b.endswith("")  # normal function


def printHelloWorld():
    print("Hello world")

# class is similar as struct, but it can also contain functions


class Student:
    # init is also called initializer/constructor, name chai thyakkai yestai hunu parcha
    # since it containd double underscore it is also called dunder method
    def __init__(self, name, age):
        self.name = name
        self.age = age


print(a, b, c, d, e, sep="\n", end="\n-------\n")
print(type(a), type(b), type(c), type(d), type(e), sep="\n", end="\n-------\n")
