#  objective:This application will display "Hello, World!" at the root URL of the website.


from flask import Flask
app = Flask(__name__)  
#   __name__ argument is passed as a Python variable that tells the application 
# where it is located on the file system.

print(__name__)

def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

@app.route('/') #python decorator 
# / leads to homepage
# user le homepage hernna chayovaney matra tala ko hello,world! print hunxa
def helloworld():
    return '<h1 style="text-align:center">Hello,world!</h1>\
        <p>This is a paragraph</p>\
        <img src="https://neupaneaayush.com.np/images/bio-photo.jpg" width=200>'
       

@app.route("/bye")
@make_bold
@make_emphasis
def say_bye():
   return "bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"
 
if __name__=="__main__":
    app.run() 

# a decorator function is simply a function which wraps another function 
# and gives it some additional functionality or
#  modifies the functionality.