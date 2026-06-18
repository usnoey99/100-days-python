## Day 44 - Creating a Beautiful Personal Site

---

### 📌 Overview
Building a beautiful personal website using HTML and CSS.

Learning how to structure web pages with divs and create layouts using positioning, sizing, font styling, and float properties.

---

### 📝 Tasks
- Use HTML div elements for page structure
- Learn CSS positioning (static, relative, absolute)
- Center elements with CSS
- Style fonts and text
- Control element sizes with CSS
- Learn how float and clear work
- Build a personal website 


---

## 🧠 Notes

### HTML Div
The `<div>` element is a generic container used to group and organize HTML elements.

It has no visual effect by itself but is commonly used for page layout and styling.

Example:

```html
<div>
    <h1>Hello</h1>
    <p>Welcome to my website.</p>
</div>
```

### CSS Position Property
The `position` property determines how an element is positioned within a document.

Common values:
* `static`
* `relative`
* `absolute`

### Static Positioning
`static` is the default positioning behavior for HTML elements.

Elements appear in the normal document flow and ignore properties such as `top`, `left`, `right`, and `bottom`.

Example:
```css
.box {
    position: static;
}
```

### Relative Positioning
`relative` positions an element relative to its normal position.

The original space occupied by the element is preserved.

Example:
```css
.box {
    position: relative;
    left: 20px;
    top: 10px;
}
```

### Absolute Positioning
`absolute` positions an element relative to its nearest positioned ancestor.

The element is removed from the normal document flow.

Example:
```css
.box {
    position: absolute;
    top: 50px;
    left: 100px;
}
```

### Centering Elements with CSS
Elements can be centered horizontally using `margin`.

Example:

```css
.container {
    width: 50%;
    margin: 0 auto;
}
```
Text can be centered using:
```css
h1 {
    text-align: center;
}
```

### Font Styling
CSS provides properties for customizing text appearance.

Common properties:

* `font-family`
* `font-size`
* `font-weight`
* `color`
* `line-height`

Example:
```css
body {
    font-family: Arial, sans-serif;
    font-size: 16px;
}
```

### CSS Sizing

Sizing properties control the dimensions of elements.

Common properties:
* `width`
* `height`
* `max-width`
* `min-width`

Example:

```css
.image {
    width: 300px;
    height: 200px;
}
```

### Float
The `float` property allows elements to be positioned to the left or right of a container.

Text and inline content can wrap around floated elements.

Example:
```css
img {
    float: left;
}
```

### Clear
The `clear` property prevents elements from wrapping around floated elements.

Example:
```css
.footer {
    clear: both;
}
```

Values:
* `left`
* `right`
* `both`

### Normal Flow
Normal flow is the default layout behavior of HTML elements.

Elements are displayed in the order they appear in the document.

Positioning and floating can change how elements behave relative to the normal flow.

### Positioned Ancestor
A positioned ancestor is an element whose `position` value is not `static`.

Absolutely positioned elements use the nearest positioned ancestor as their reference point.

Example:
```css
.parent {
    position: relative;
}
.child {
    position: absolute;
    top: 20px;
    left: 20px;
}
```

