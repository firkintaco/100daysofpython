from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.String)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


with app.app_context():
    db.create_all()
    # db.session.add(second_movie)
    # db.session.commit()

class updateForm(FlaskForm):
    review = StringField(label='Review', validators=[DataRequired()])
    rating = StringField(label='Rating', validators=[DataRequired()])
    submit = SubmitField(label='Send')

class addForm(FlaskForm):
    title = StringField(label="Title",validators=[DataRequired()])
    year = IntegerField(label='Year',validators=[DataRequired()])
    description = StringField(label='Description',validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    ranking = IntegerField(label='Ranking',validators=[DataRequired()])
    rating = StringField(label='Rating', validators=[DataRequired()])
    img_url = StringField(label="Image Url",validators=[DataRequired()])
    submit = SubmitField(label='Add')


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    print(movies)
    return render_template("index.html", movies=movies)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = addForm()
    if form.validate_on_submit():
        movie_to_add = Movie(title=form.data["title"], year=form.data["year"], description=form.data["description"],
                             review=form.data["review"], ranking=form.data["ranking"], rating=form.data["rating"], img_url=form.data["img_url"])
        db.session.add(movie_to_add)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    form = updateForm()
    movie_to_edit = db.get_or_404(Movie, id)
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.errors)
            review = form.data["review"]
            rating = form.data["rating"]
            movie_to_edit.rating = rating
            movie_to_edit.review = review
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('edit.html', form=form, movie=movie_to_edit)

@app.route("/delete")
def delete():
    id = request.args.get('id')
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
