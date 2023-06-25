from flask import Flask
from markupsafe import escape
from random import randint

app = Flask(__name__)
print(__name__) # Print __main__
random_number = randint(0,9)
# Python Decorator
@app.route("/")
def frontpage():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"

@app.route("/<int:number>")
def show_page(number):
    if number == random_number:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif number < random_number:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    elif number > random_number:
        return "<h1 style='color:purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"



if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)