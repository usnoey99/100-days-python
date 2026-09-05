# Day 71 - Publishing our Flask Website

---

## 📌 Overview
Publish the Flask blog website using Heroku, GitHub, and Gunicorn.  
Upgrade the database from SQLite to PostgreSQL for production.

---

## 🧠 Note

### Gunicorn
Flask's built-in development server is intended for development and testing.  

For production, the application should use a production WSGI server such a Gunicorn.  

The start command can be:
```text
gunicorn main:app
```
The `main` refers to the Python file `main.py`.
The `app` refers to the Flask application object: `app = Flask(__name__)`


### PostgreSQL
The project originally uses SQLite for local development.  
SQLite and PostgreSQL are both relational database systems, but they are designed for different purposes.  

SQLite stores the database as a local file:
```text
Flask
  ↓
SQLite
  ↓
blog.db
```

For production, the database is upgraded to PostgreSQL:
```text
Flask
  ↓
PostgreSQL Server
  ↓
Database
```
PostgreSQL runs as a separate database server that the Flask application connects to.  

PostgreSQL is suitable for:

- Production applications
- Multiple users
- Concurrent database operations
- Larger amounts of data
- Applications that need advanced database features

A blog website can have many users accessing the database at the same time.  
PostgreSQL is designed to handle concurrent connections and database operations more effectively than SQLite.  


### Free Hosting Providers
**Render**  
A hosting platform for deploying web applications such as Flask, Django, and Node.js.  
It offers a free plan and can be connected to GitHub for easy deployment.

**Vercel**  
A platform mainly focused on frontend and serverless applications.  
It offers a free Hobby plan and is especially suitable for JavaScript and Next.js projects.

**PythonAnywhere**  
A hosting platform designed specifically for Python applications.  
It offers a free Beginner plan and supports Python web frameworks such as Flask and Django.