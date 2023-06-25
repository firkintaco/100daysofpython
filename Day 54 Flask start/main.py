from flask import Flask

app = Flask(__name__)
print(__name__) # Print __main__

# Python Decorator
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<h1>Bye Bye</h1>"

if __name__ == "__main__":
    app.run()