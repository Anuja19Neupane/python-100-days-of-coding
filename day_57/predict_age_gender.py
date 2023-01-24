from flask import Flask, render_template
import random
import datetime


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    return render_template("guess.html", your_name=name)


@app.route("/blog")
def blogs():
    blogs = [

        {

            'userId': 1,
            'id': 1,
            'title': "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            'body': '''quia et suscipit
                        suscipit recusandae consequuntur expedita et cum
                        reprehenderit molestiae ut ut quas totam
                        nostrum rerum est autem sunt rem eveniet architecto'''
        },
        
          {

            'userId': 1,
            'id': 1,
            'title': "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            'body': '''quia et suscipit
                        suscipit recusandae consequuntur expedita et cum
                        reprehenderit molestiae ut ut quas totam
                        nostrum rerum est autem sunt rem eveniet architecto'''
        },

          {

            'userId': 1,
            'id': 1,
            'title': "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            'body': '''quia et suscipit
                        suscipit recusandae consequuntur expedita et cum
                        reprehenderit molestiae ut ut quas totam
                        nostrum rerum est autem sunt rem eveniet architecto'''
        },

          {

            'userId': 1,
            'id': 1,
            'title': "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            'body': '''quia et suscipit
                        suscipit recusandae consequuntur expedita et cum
                        reprehenderit molestiae ut ut quas totam
                        nostrum rerum est autem sunt rem eveniet architecto'''
        },


    ]


    return render_template("blog.html",blogs=blogs )

if __name__ == "__main__":
    app.run()
