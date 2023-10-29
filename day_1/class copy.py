# normal function
def printHelloWorld(): #function fall 
    print("Hello world")

# class is similar as struct, but it can also contain functions


class Student:
    # init is also called initializer/constructor, name chai thyakkai yestai hunu parcha
    # since it containd double underscore it is also called dunder method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # this will define the behavior of the object when we use addition operator (+)
    def __add__(self, other):
        return Student(self.name+other.name, self.age+other.age)

    # this is define the behaviour when we try to print our custom object
    def __repr__(self):
        return f"Name={self.name},age={self.age}"

    # this is function but since it is defined inside the class, it is called method
    # it can be called from the object using dot(.) operator
    def printName(self):
        print(self.name)


# Student is class but a and b are object,
# object is created by instantiation of the class
#  when we instantiate object from class like this, __init__ method is called
a = Student("Aayush", 21)
b = Student("Anuja", 17)

#  this his how we call the method of the class
a.printName()
b.printName()
