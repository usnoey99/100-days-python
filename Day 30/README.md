## Day 30 - Errors, Exceptions and Saving JSON Data

---

### 📌 Overview
Learned how to handle different types of errors and prevent the application from crashing by using exception handling.  
Also explored JSON data format, which is widely used for storing and exchanging data between applications over the internet.

---

### 📝 Tasks
- Improved Password Manager by adding a website search feature  
  → Returns the email and password associated with a specific website
- Implemented error handling to prevent the program from crashing
- Added JSON file handling for saving and retrieving user data

---

## 🧠 Notes

### Errors
- FileNotFoundError:
  Raised when trying to open a file that does not exist.

- KeyError:
  Raised when accessing a dictionary key that does not exist.

- IndexError:
  Raised when accessing a list index that is out of range.

- TypeError:
  Raised when using an operation on an incompatible data type.

### Catching Exceptions
- try: Something that might cause an exception.
- except: Do this if there **was** an exception.
- else: Do this if there were **no** exceptions
- finally: Do this no matter what happens.

### Raising Exceptions
- raise: Manually creates and raises an exception.

Example:
```python
if age < 18:
    raise ValueError("You must be at least 18 years old.")

score = -5
if score < 0:
    raise ValueError("Score cannot be negative.")
```

### JSON
A lightweight format used to store and exchange data.

Example:
```json
{
  "name": "John",
  "age": 25,
  "is_student": true
}
```
- `json.dump()`:
  Writes Python data into a JSON file.
  ```json
  import json
  data = {"name": "John", "age": 25}
  with open("data.json", "w") as file:
    json.dump(data, file)
  ```

- `json.load()`:
  Reads JSON data from a file and converts it into a Python object.
  ```json
  with open("data.json", "r") as file:
      data = json.load(file)
  ```
- `json.update()`:
  Not a JSON function. It is a Python dictionary method used to update key-value pairs.
  ```json
  data = {"name": "John"}
  data.update({"age": 25})
  ```
  Since JSON files cannot be partially updated, the workflow is:
  - Load existing data
  - Update dictionary in Python
  - Save the entire data back to the file

### JSON vs Python Dictionary

| Feature | JSON | Python Dictionary |
|--------|------|------------------|
| Type | Data format (text) | Python object (in memory) |
| Purpose | Data storage / transfer | Program logic |
| Quotes | Double quotes only | Single or double quotes |
| Usage | Files, APIs, communication | Inside Python code |
