from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if email already exists
        existing_user = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()

        if existing_user:
            flash("That email is already registered. Please login.")
            return redirect(url_for('login'))

        # Hash password
        hashed_password = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            name=request.form["name"],
            email = request.form["email"],
            password = hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        # Find user by email
        user = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()

        # User does not exist
        if not user:
            flash("This email does not exist. Please check your email and try again.")
            return redirect(url_for('login'))

        # Wrong password
        if not check_password_hash(user.password, password):
            flash("Incorrect password. Please try again.")
            return redirect(url_for('login'))

        # Login successful
        login_user(user)
        return redirect(url_for('secrets'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    directory=os.path.join(app.static_folder, 'files')
    path="cheat_sheet.pdf"
    return send_from_directory(directory,path)


if __name__ == "__main__":
    app.run(debug=True)
