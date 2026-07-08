# Day 58 - Bootstrap

---

## 📌 Overview
Learned how to use Bootstrap, a popular frontend toolkit, to build responsive and visually appealing web pages.  
Used Bootstrap components, the grid system, and utility classes to simplify page layouts while reducing the amount of custom CSS required.  
Applied these concepts by recreating the TinDog landing page.

---

## 📝 Tasks
* Learn the basics of Bootstrap
* Include Bootstrap via CDN
* Use Bootstrap's grid system for responsive layouts
* Apply built-in Bootstrap components
* Customize page layouts using Bootstrap utility classes
* Build a responsive landing page with Bootstrap
* Reduce custom CSS by leveraging Bootstrap styles


---

## 🧠 Notes

### Bootstrap
Bootstrap is a popular frontend toolkit that provides pre-designed CSS classes and JavaScript components for building reponsice websites.  
Instead of writing large amounts of custom CSS, we can apply Bootstrap classes directly to HTML elements.  

Example:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
```

### Bootstrap Grid System
Bootstrap uses a 12-column grid system to create responsice layouts.  
```html
<div class="container">
    <div class="row">
        <div class="col">
            Column 1
        </div>
        <div class="col">
            Column 2
        </div>
    </div>
</div>
```
The grid automatically adjusts based on the screen size.

### Containers
Bootstrap provides responsive containers to center and pad page content.
Common container classes:  
- `container` – Responsive fixed-width container
- `container-fluid` – Full-width container spanning the entire viewport


Example:
```html
<div class="container">
    Content
</div>
```

### Responsive Breakpoints
Bootstrap uses responsive breakpoints to change layouts based on screen size.  

Common breakpoints:

| Prefix | Screen Width |
| ------- | ------------ |
| `sm` | ≥576px |
| `md` | ≥768px |
| `lg` | ≥992px |
| `xl` | ≥1200px |
| `xxl` | ≥1400px |

Example:

```html
<div class="col-12 col-md-6 col-lg-4">
```
This element takes:
- 12 columns on small screens
- 6 columns on medium screens
- 4 columns on large screens

### Utility Classes
Bootstrap includes utility classes for spacing, alignment, colors, sizing, and typography.  
Example:
```html
<div class="text-center mt-5">
    <h1 class="text-primary">
        Hello Bootstrap
    </h1>
</div>
```
Common utility classes include:

- `mt-*`, `mb-*`, `p-*` for margin and padding
- `text-center` for text alignment
- `d-flex` for Flexbox layouts
- `justify-content-*` and `align-items-*` for alignment
- `bg-*` and `text-*` for colors

### Bootstrap Buttons
Bootstrap provides predefined button styles.  

Example:

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline-dark">Outline</button>
```

### Bootstrap Icons
Bootstrap Icons can be used as SVGs or through an icon library.  

Example:

```html
<svg class="bi bi-apple">
    ...
</svg>
```
They integrate well with Bootstrap components such as buttons and navigation bars.