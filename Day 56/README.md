# Day 56 - Static files, HTML/CSS File Rendering and a Personal Site

---

## 📌 Overview
Learned how to serve static files such as local images and videos in a Flask application, and how to render HTML and CSS files.  
Applied these concepts by building a simple personal business card website as the final project.

---
## 📝 Tasks
* Set up Flask project structure with `templates` and `static` folders
* Serve static files (images, videos, CSS) using Flask
* Link external CSS files to HTML templates
* Render HTML pages using `render_template()`
* Build a personal business card website


### ✨ Additional Features
- 

---

## 🧠 Notes

### Serving Static Files
Flask serves static files such as CSS, JavaScript, images, and videos from the `static/` directory.  
Project structure:
```text
project/ 
│ 
├── app.py 
├── static/ 
│ ├── css/ 
│ ├── images/ 
│ └── videos/ 
└── templates/ 
  └── index.html
```
Use `url_for()` to generate the correct path to a static file.  
Example:
```html
<img src="{{ url_for('static', filename='images/profile.jpg') }}">

<video controls>
    <source src="{{ url_for('static', filename='videos/demo.mp4') }}" type="video/mp4">
</video>
```
Using `url_for()` is recommended instead of hardcording file paths because Flask automatically generates the correct URL for static resources.