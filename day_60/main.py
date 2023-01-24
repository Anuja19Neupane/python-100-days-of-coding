from flask import Flask,request, render_template
import requests

# The Request, in Flask, is an object that contains all the data sent from the Client to Server.
#  This data can be recovered using the GET/POST Methods.

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        return f"<h1>Name: {name}, Password: {password}</h1>"

    elif request.method == "GET":
        return render_template("index.html")

        

if __name__ == "__main__":
    app.run()
