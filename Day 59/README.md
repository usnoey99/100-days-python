# Day 59 - Blog Capstone Project Part 2

---

## 📌 Overview
Built the second part of the Blog Capstone Project using a Bootstrap template.  
Created a multi-page blog website with a responsive navigation bar, dynamically generated blog post pages, and a full-width hero section displaying each post title.  
Ensured the layout adapts seamlessly across different screen sizes.

---

## 📝 Tasks
* Download and organize the starter project files
* Render the homepage locally using Flask
* Create reusable header and footer templates
* Use Jinja's `include` statement for template rendering
* Build the About and Contact pages
* Fetch blog posts from an API and display them on the homepage
* Render individual blog post pages dynamically


---

## 🧠 Notes

### Jinja Template Inheritance and Includes
Jinja allows reusable HTML components by using `include`.  

Instead of repeating navigation bars and footers across multiple pages, they can be separated into individual templates.  

Example:
```html
{% include 'header.html' %}
```
This improves code organization and reduces duplication.

### Dynamic URLs in Flask
Flask can create dynamic routes using route parameters.  

Example:
```python
@app.route('/post/<int:p_id>')
def get_post(p_id):
    return render_template(
        'post.html',
        post=all_posts[p_id - 1]
    )
```

The URL changes based on the post ID:
```text
/post/1
/post/2
/post/3
```
Jinja can generate these URLs dynamically:
```html
<a href="{{ url_for('get_post', p_id=post.id) }}">
    {{ post.title }}
</a>
```

### Rendering Dynamic Content with Jinja
Jinja allows Python data to be displayed inside HTML templates.  

Example:
```html
{% for post in posts %}

<h2>{{ post.title }}</h2>
<p>{{ post.subtitle }}</p>

{% endfor %}
```
The loop automatically creates multiple blog post previews based on the API data.

### Bootstrap Responsive Layout
Bootstrap's grid system was used to create responsive blog layouts.  

Example:
```html
<div class="col-md-10 col-lg-8 col-xl-7">
```
The layout changes depending on screen size:
- md → Medium devices
- lg → Large devices
- xl → Extra large devices

This allows the blog content to remain readable across different screen sizes.