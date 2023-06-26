from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    return render_template("index.html", year=year)

@app.route("/guess/<name>")
def agify(name):
    response = requests.get(url="https://api.agify.io", params={"name":name})
    data = response.json()
    gender = requests.get(url="https://api.genderize.io", params={"name":name}).json()["gender"]
    print(gender)
    return render_template("guess_page.html", data=data, gender=gender)

@app.route("/blog/<blogId>")
def get_posts(blogId):
    print(blogId)
    posts = requests.get(url="https://api.npoint.io/510fc914970f36c49103").json()
    return render_template("blogs.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)


