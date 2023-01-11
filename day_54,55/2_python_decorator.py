import time

def delay_decorator(function):
    def wrapped_function():
        time.sleep(2) # given below functions harulai 2 second late display garna xa vaney we use python decorator

        function()
    return wrapped_function

@delay_decorator # mathi gareko delay yaha apply hunxa
def say_hello():
    print("hello")


def say_bye():
    print("bye")

decorated_function=delay_decorator(say_bye)
decorated_function() #   @delay_decorator   garnu ra yo line 18 and 19 garnu same ho