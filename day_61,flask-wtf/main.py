from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email' ,validators=[DataRequired()]) # stringfield le password show garxa
    password = PasswordField(label='Password', validators=[DataRequired()]) # PasswordField le passsword show gardaina
    submit=SubmitField(label='Log In')
    # The first argument passed to the StringField constructor is the label for the field, 
    # which will be displayed as a placeholder or label on the form in the web page.



app = Flask(__name__)
Bootstrap(app)
app.secret_key="mysecretkey"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login" , methods=["GET","POST"])
def login():
    login_form = LoginForm()
    # login_form is variable
    # LoginFormis class
    #  yeso garda LoginForm class ko new object create hunxa ani login_form variable ma assign hunxa
    if login_form.validate_on_submit():
        your_email=login_form.email.data
        print(f"Your email is: {your_email}")
        if login_form.email.data == "forpython959@gmail.com" and login_form.password.data == "mysecretkey":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)



app.secret_key="mysecretkey"


if __name__ == '__main__':
    app.run()