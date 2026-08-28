# Day 68 - User Authentication and Registration

---

## 📌 Overview
Learn how to register, log in, and log out users using email and password authentication.  
Restrict access to user profile pages and allow only registered users to download a confidential Flask programming cheat sheet.

---

## 🎬 Demo

### Add Post
<img src="static/assets/img/demo_newPost.gif" width="400">

### Edit Post
<img src="static/assets/img/demo_editPost.gif" width="400">

### Delete Post
<img src="static/assets/img/demo_deletePost.gif" width="400">

---

## 📝 Tasks

* 

---

## 🧠 Note

### app.static_folder
It returns the path to Flask's `static` folder.  
It can be combined with `os.path.join()` to safely create the path to files inside the static directory.  
```python
import os

directory = os.path.join(app.static_folder, "files")
return send_from_directory(
    directory=directory,
    path="cheat_sheet.pdf"
)
```
The path becomes:
```text
static/files/cheat_sheet.pdf
```

### target="_blank"
The `target="_blank"` attribute opens the linked page in a new browser tab.
```html
<a href="{{ url_for('download') }}" target="_blank">
    Download Your File
</a>
```
If you want PDFs to be downloaded rather than displayed directly in the browser, add `as_attachment=True` to `send_from_directory()`:
```python
return send_from_directory(
    directory=directory,
    path="cheat_sheet.pdf",
    as_attachment=True
)
```

### Hashing Function
Hashing is a one-way process that converts a password into a fixed-length hash value.  
Unlike encryption, a hashed password cannot be decrypted back into the original password.  

Instead of storing the user's original password, we store the hashed password in the database.
```python
from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash(password)
```
When the user logs in, the entered password is checked against the stored hash using `check_password_hash()`.
```python
from werkzeug.security import check_password_hash
check_password_hash(stored_hash, password)
```
The password is never decrypted. The hashing function verifies whether the entered password matches the stored hash.

### Salting
**Saltin** is the process of adding a unique, random value to a password before hashing it.  
Without salting, two users with the same password would produce the same hash.  
With salting:
```text
password + random salt → hash → different hash
```
The salt is stored along with the password hash, so it can be used again when verifying the password.  
