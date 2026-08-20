from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# # Create database and table
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY,
#         title TEXT NOT NULL,
#         author TEXT NOT NULL,
#         rating REAL NOT NULL
#     )
# """)
#
# db.commit()
# db.close()

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-book-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Create Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# Create database and table
with app.app_context():
    db.create_all()

    # # Add the first book
    # new_book = Book(
    #     id=1,
    #     title="Harry Potter",
    #     author="J.K.Rowling",
    #     rating=9.3
    # )

    # db.session.add(new_book)
    # db.session.commit()


@app.route("/")
def home():
    # db = sqlite3.connect("books-collection.db")
    # cursor = db.cursor()hksrP
    #
    # cursor.execute("SELECT * FROM books")
    # all_books = cursor.fetchall()
    #
    # db.close()

    all_books = db.session.execute(db.select(Book)).scalars().all()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]

        # db = sqlite3.connect("books-collection.db")
        # cursor = db.cursor()
        #
        # cursor.execute(
        #     "INSERT INTO books (title, author, rating) VALUES (?, ?, ?)",
        #     (title, author, rating)
        # )
        #
        # db.commit()
        # db.close()

        new_book = Book(
            title=title,
            author=author,
            rating=rating
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id)

    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.rating = request.form["rating"]

        db.session.commit()

        return redirect(url_for("home"))
    return render_template("edit.html", book=book)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = db.get_or_404(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)