from flask import Flask, render_template
import requests
from post import Post
posts = requests.get(url="https://api.npoint.io/69a6ea61064474d9c520").json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"], post["image"], post["author"], post["date"]) for post in posts]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:postId>')
def get_post(postId):
    requested_post = None
    for post in post_objects:
        if post.id == postId:
            requested_post = post
    return render_template('post.html', post=requested_post)

@app.route("/about-me")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
