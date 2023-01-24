from flask import Flask,request, render_template
import random
import datetime
import requests

posts=requests.get("https://api.npoint.io/5f2217674ea5b6004cf6")
post_blogs=posts.json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html" ,posts=post_blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["GET","POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return "<h1>Successfully sent your Message.</h1>"

    elif request.method == "GET":
        return render_template("contact.html")    




if __name__ == "__main__":
    app.run()