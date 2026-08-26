# Day 66 - Building My Own REST API Service

---

## 📌 Overview

Learn how to build a complete REST API sevice using Flask, starting from the fundamentals.  
The project covers the basic concepts of REST APIs and how to create, handle and serve API endpoints with Flask.

API Document: https://documenter.getpostman.com/view/57738866/2sBYAsysgP

---

## 📝 Tasks

* Build a REST API using Flask and SQLite with SQLAlchemy
* Create API endpoints for retrieving cafe data
* Return cafe data as JSON using `jsonify()`
* Serialize SQLAlchemy objects into dictionaries and JSON
* Use query parameters to search for cafes by location
* Create a `POST` endpoint to add a new cafe
* Use `PATCH` to update a cafe's coffee price
* Use `DELETE` to remove a closed cafe
* Add API key authentication to protect the delete endpoint
* Return appropriate HTTP status codes for errors
* Test API endpoints and create API documentation using Postman

---

## 🧠 Note

### REST API
REST (Representational State Transfer) is an architectural style for building web services.  

A REST API allows clients and servers to communicate using HTTP requests.  

Common HTTP methods include:
- `GET` - Retrieve data
- `POST` - Create new data
- `PUT` - Update existing data
- `PATCH` - Partially update existing data
- `DELETE` - Delete data


### Flask API Endpoint
Flaks can be used to create API endpoints by defining routes that handle HTTP requests.
```python
@app.route("/api/users", methods=["GET"])
def get_users():
    return {"users": users}
```
The endpoint can then be accessed by sending a `GET` request to `/api/users`.

### Postman
A tool for testing APIs.  
Postman lets us send HTTP requests directly to our Flask server and see the response.

### PUT vs PATCH
Both `PUT` and `PATCH` and HTTP methods used to update existing resources.  
`PUT` is generally used to replace the entire resource, while `PATCH` is used to update only specific fields.
