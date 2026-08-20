# Day 63 - Database & SQLite / SQLAlchemy

---

## 📌 Overview
Built a Virtual Bookshelf web application for recording books I have read and rating each book.

Inspired by LibraryThing, this project focuses on learning how to use databases with Flask.

The main goal of this project is to learn how to create and manage an SQLite database, perform CRUD operations, and connect the database to a Flask application so that data can be stored and retrieved whenever needed.

---

## 📝 Tasks

* Create an SQLite database
* Create a database table for books
* Add new books to the database
* Read and display book data
* Update book information and ratings
* Delete books from the database
* Connect the database to the Flask application
* Display stored books using Flask and Jinja
* Create a simple virtual bookshelf interface

---

## 🧠 Note

### SQLAlchemy
**SQLAlchemy** can map relationships in a database to objects.  
- Table → Class
- Column → Object Attribute
- Row → Object

For example, a `books` table can be represented by a Python `Book` class.
```python
class Book(db.Model):
    title = db.Column(db.String(250))
    author = db.Column(db.String(250))
    rating = db.Column(db.Float)
```
Each row in the database can then be represented as a `Book` object:
```python
book = Book(
    title="Harry Potter",
    author="J.K. Rowling",
    rating=9
)
```
We can access the data through the object's attributes:
```text
book.title
book.author
book.rating
```

### CRUD with SQLAlchemy
CRUD stands for:
- Creat → Add new data
  ```python
  new_book = Book(
      title="Harry Potter",
      author="J.K. Rowling",
      rating=9.3
  )

  db.session.add(new_book)
  db.session.commit()
  ```

- Read → Retrieve data
  ```python
  all_books = db.session.execute(
    db.select(Book)
  ).scalars().all()
  ```
  Because SQLAlchemy returns `Book` objects, we can access their attributes directly: book.title
- Update → Modify existing data
  ```python
  book = db.get_or_404(Book, book_id)
  
  book.title = "Harry Potter"
  book.author = "J.K. Rowling"
  book.rating = 9.5
  
  db.session.commit()
  ```
- Delete → Remove data
  ```python
  book = db.get_or_404(Book, book_id)
  
  db.session.delete(book)
  db.session.commit()
  ```
