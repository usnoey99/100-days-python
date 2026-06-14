## Day 41 - Creating Websites with HTML

---

### 📌 Overview
Today I learned the fundamentals of HTML (HyperText Markup Language) and created a simple personal website.

The website includes a profile image, headings, paragraphs, hyperlinks, lists, and navigation to another page. Through this project, we explored how HTML structures content and how different elements work together to build a webpage.

---

### 📝 Tasks
- Create a simple personal website
- Learn the basic structure of HTML documents
- Add images, links, and lists to a webpage
- Connect multiple pages using hyperlinks
- Practice using common HTML tags

---

## 🧠 Notes

### HTML
HTML stands for **HyperText Markup Language**.

It is the standard markup language used to create web pages and structure content on the internet.

Example:
```html
<h1>Hello World</h1>
```

### Basic HTML Structure
Every HTML document follows a standard structure.
```html
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
</head>
<body>

</body>
</html>
```
| Element           | Purpose                       |
| ----------------- | ----------------------------- |
| `<!doctype html>` | Declares HTML5                |
| `<html>`          | Root element                  |
| `<head>`          | Metadata and page information |
| `<body>`          | Visible webpage content       |

### The `<head>` Section
Contains information about the webpage that is not displayed directly.

```html
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
</head>
```
`<meta charset="UTF-8">`: Defines character encoding.
- Supports international charaters.
- Supports emojis.
- Prevents text display issues.

### The <body> Section
Contains everything visible on the webpage.

### Images
The `<img>` tag display images.
Example:
```html
<img src="computer-image.jpg" alt="computer science image">
```
The `alt` text also improves accessibility for screen readers.

| Attribute | Purpose                               |
| --------- | ------------------------------------- |
| `src`     | Image location                        |
| `alt`     | Alternative text if image cannot load |

### Paragraphs
The `<p>` tag creates paragraphs.
Paragraphs automatically create spacing between blocks of text.

### Text Formatting
- `<em>` used for emphasized text.
- `<strong>` used for important text.

### Hyperlinks
The `<a>` tag creates clickable links.
```html
<a href="https://github.com"
   target="_blank"
   rel="noopener noreferrer">
```
- `target="_blank"`: Opens the link in a new browser tab.
- `rel="noopener noreferrer"`: Improves security when opening links in a new tab.
