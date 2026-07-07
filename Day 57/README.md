# Day 57 - URL Building and Templating with Jinja in Your Flask Application

---

## 📌 Overview
Learned how to use Jinja, Flask's template engine, to create dynamic web pages.  
Applied template rendering, variable passing, conditional statements, loops, and URL building with `url_for()` to build a simple blog application.

---
## 📝 Tasks
* Learn how Flask uses Jinja templates to render dynamic HTML content
* Pass Python variables to HTML templates using `render_template()`
* Display dynamic data using Jinja variable syntax
* Use Jinja conditional statements and loops
* Build dynamic URLs using `url_for()`
* Fetch blog post data from an API and display posts using templates
* Create individual blog post pages using dynamic routes

---

## 🧠 Notes

### Jinja Template Engine
Jinja is the template engine used by Flask.  
It allows to pass Python data to HTML templates and render dynamic content.

Example:
```python
@app.route("/")
def home():
    return render_template("guess.html", name="Alice")
```

`index.html`:
```html
<h1>Hello {{ name }}</h1>
```

Output:
```text
Hello Alice
```

`{{ }}` is used to display variables in a template.  
You can also pass multiple variables to a template through `render_template()`.

### Jinja Conditional Statements
Example:
```python
@app.route("/")
def home():
    return render_template("guess.html", logged_in=True)
```

`index.html`:
```html
{% if logged_in %}
    <h1>Welcome!</h1>
{% else %}
    <h1>Please Login</h1>
{% endif %}
```
`{% %}` is used for control structures such as conditional statements and loops.

### Jinja Loops
Example:
```python
@app.route("/")
def home():
    fruits = ["Apple", "Banana", "Orange"]
    return render_template("guess.html", fruits=fruits)
```

`index.html`:
```html
<ul>
{% for fruit in fruits %}
    <li>{{ fruit }}</li>
{% endfor %}
</ul>
```
Output:
```text
Apple
Banana
Orange
```

### Passing Objects to Templates
Python objects can also be passed to templates and accessed using dot notation.

Python:
```python
post = Post(1, "Title", "Subtitle", "Body")

return render_template(
    "blog.html",
    post=post
)
```

Jinja:
```python
<h1>{{ post.title }}</h1>
<h2>{{ post.subtitle }}</h2>
<p>{{ post.body }}</p>
```

