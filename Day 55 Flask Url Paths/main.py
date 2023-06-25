from flask import Flask
from markupsafe import escape

app = Flask(__name__)
print(__name__) # Print __main__

# Python Decorator
@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
           "<p>This is paragraph</p>"

def title_decorator(function):
    def wrapper_func():
        return f"<h1>{function()}</h1>"
    return wrapper_func

def make_bold(func):
    def wrapper():
        return "<b>"+func()+"</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>"+func()+"</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# Different routes using the app.route decorator
@app.route("/bye")

# Styling text using decorators
@title_decorator
@make_bold
@make_underlined
def say_bye():
    return "Bye Bye"

# Creating variable paths and converting the path to a specified data type
@app.route("/<name>/<int:number>")
def show_page(number):
    return f"{number}"

@app.route("/user/<username>")
def user_home(username):
    return "Hello {}".format(escape(username).title())

@app.route("/randompath")
def page():
    return "Hei"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)