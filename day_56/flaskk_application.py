from flask import Flask,render_template
import time


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
   
@app.route("/cv") 
def cv():
     return render_template("anuja.html")





if __name__=="__main__":
    app.run()
