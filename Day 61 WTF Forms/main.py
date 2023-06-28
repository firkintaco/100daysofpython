from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "some secret string"
Bootstrap(app)
class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), InputRequired()])
    password = PasswordField('password', validators=[DataRequired(), InputRequired()])
    submit = SubmitField(label="Login")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        if loginForm.name.data == "Admin" and loginForm.password.data == "1234":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=loginForm)

if __name__ == '__main__':
    app.run(debug=True)