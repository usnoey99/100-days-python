# Day 60 - Flask POST Requests & Contact Form

---

## 📌 Overview
Built a functional contact form using HTML and Flask.  
Created an HTML form to collect user input, handled form submissions with Flask's POST method, and sent contact messages via email using Python's `smtplib`.  
This project demonstrates how frontend forms communicate with a backend server and how submitted data can trigger real-world actions.


---

## 📝 Tasks
* Build a contact form using HTML
* Create input fields for user information
* Handle form submissions with Flask's POST request
* Process submitted form data on the server
* Send emails using Python's `smtplib`
* Display a success message after form submission
* 
---

## 🧠 Notes

### HTML Forms
HTML forms collect user input and send it to a server.

Example:

```html
<form action="{{ url_for('contact') }}" method="POST">
  <input type="text" name="name" placeholder="Your Name">
  <input type="email" name="email" placeholder="Your Email">
  <textarea name="message"></textarea>
  <button type="submit">Send</button>
</form>
```

The `method="POST"` attribute sends the form data securely in the request body.

### HTML Form Attributes: `action` and `method`
HTML forms must specifu where and how to send user input.  

Example:
```html
<form action="/login" method="POST">
    ...
</form>
```
- `action` specifies the URL that receives the submitted data.
- `method` specifies the HTTP request method.
- Without these attributes, the form cannot send data correctly to the Flask server.

### POST Request
A POST request sends data from the client to the server.  

Unlike a GET request, which places data in the URL,
```text
/login?username=Tom
```
a POST request sends the data inside the request body.  

This is commonly used for:
- Login forms
- Contact forms
- Registration forms
- Any form that submits user input

### Handling POST Requests in Flask
Flask can process form data using the `request` object.

Example:

```python
from flask import request

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
```

The submitted values are accessed through `request.form`.