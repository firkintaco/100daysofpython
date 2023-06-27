from flask import Flask, render_template, request
import requests
from post import Post
import smtplib
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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="curiousmindlabs@gmail.com", password="")
            connection.sendmail(from_addr="curiousmindlabs@gmail.com", to_addrs="pythonmaster2023@yahoo.com", msg=f"Subject: New Contact form\n\nName: {name}\nEmail: {email}\nMessage: {message}\nSent from blog")
        return render_template("contact.html", sended=True)
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
