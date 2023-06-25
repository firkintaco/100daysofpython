from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/user/<name>")
def homepage(name=None):
    return render_template("./index.html", name=name)

@app.route("/cv")
def cv():
    return render_template("template.html")
if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)