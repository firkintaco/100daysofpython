from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
# configure the SQLite DB, relative to app folder
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///books.db'
db.init_app(app)

# Define db model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book title={book.title} author={self.author} rating={self.rating}>"

# with app.app_context():
    # db.create_all()
    # book_to_add = Book(title="Harri Pötkylä", author="J. K. Rowling", rating=9.3)
    # db.session.add(book_to_add)
    # db.session.commit()
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    print(book)


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    books_count = 2
    print(all_books)
    return render_template('index.html', all_books=all_books, books_count=books_count)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form['book']
        author_name = request.form['author']
        book_rating = request.form.get('rating')
        book = Book(title=book_name,author=author_name,rating=book_rating)
        db.session.add(book)
        db.session.commit()
        return redirect("/")
    return render_template('add.html')

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        new_rating = request.form['new_rating']
        book_to_update = db.get_or_404(Book, id)
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect("/")
    bookDetails = db.get_or_404(Book, id)
    print(bookDetails)

    return render_template('edit.html', book=bookDetails)

@app.route("/delte")
def delete():
    book_id = request.args.get('id')

    # Get book to delete
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

