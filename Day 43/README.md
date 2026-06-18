## Day 43 - Styling websites with CSS

---

### 📌 Overview
Learning how to style websites using CSS.

Upgrading a personal CV website by applying colors, fonts, spacing, borders, and other visual styles. Learning how CSS separates presentation from structure and improves the appearance of web pages.

---

### 📝 Tasks
- Apply CSS to an existing HTML CV website
- Connect an external stylesheet to an HTML document
- Style text, colors, and page layout
- Use CSS selectors to target specific elements
- Apply classes and IDs for custom styling
- - Debug CSS styling issues using browser tools
- Improve the overall appearance of the CV website


---

## 🧠 Notes

### CSS (Cascading Style Sheets)
CSS is a stylesheet language used to control the presentation and appearance of HTML documents.

It controls how HTML elements are displayed, including colors, fonts, spacing, layouts, and other visual styles.

### Inline CSS

Inline CSS applies styles directly to an HTML element using the style attribute.

Example:
```
<h1 style="color: blue;">Hello World</h1>
```
- Applies to a single element
- Highest specificity
- Not recommended for large projects because it is difficult to maintain

### Internal CSS
Internal CSS is written inside a <style> tag within the HTML document.

Example:
```
<head>
    <style>
        h1 {
            color: blue;
        }
    </style>
</head>
```
- Styles apply only to the current page
- Useful for small projects or testing

### External CSS
External CSS is stored in a separate .css file and linked to an HTML document.

HTML:
```
<link rel="stylesheet" href="style.css">
```
CSS:
```
h1 {
    color: blue;
}
```
- Reusable across multiple pages
- Easier to maintain
- Most common approach in web development

### Class Selector
A class selector targets elements that share the same class name.
HTML:
```
<h2 class="important">Important</h2>
```
CSS:
```
.important {
    color: red;
}
```
- Begins with a period (`.`)
- Can be reused on multiple elements

### ID Selector
An ID selector targets a single unique element.

HTML:
```
<h1 id="title">My Website</h1>
```
CSS:
```
#title {
    color: blue;
}
```
- Begins with a hash symbol (`#`)
- Should be unique within a page

### Classes vs. IDs

Class:
- Uses `.classname`
- Can be applied to multiple elements
- Used for reusable styles

ID:
- Uses `#idname`
- Should be used only once per page
- Used for unique elements

Example:
```
<h1 id="main-title">Portfolio</h1>

<p class="highlight">First paragraph</p>
<p class="highlight">Second paragraph</p>
```

### CSS Specificity
Specificity determines which CSS rule is applied when multiple rules target the same element.

Priority (highest to lowest):
1. Inline CSS
2. ID Selector
3. Class Selector
4. lement Selector

Example:
```
<h1 id="title" class="heading" style="color: red;">
    Hello
</h1>
```
The text will be red because inline CSS has the highest priority.

### Debugging CSS
Debugging CSS is the process of finding and fixing styling issues.

Common checks:
- Verify that the CSS file is correctly linked
- Check for spelling mistakes in selectors
- Confirm that class and ID names match
- Inspect elements using browser Developer Tools
- Check specificity conflicts between rules