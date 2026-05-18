## Day 24 - Working with Local Files and Directories

---

### 📌 Overview
Improving the previous Snake Game project by adding a high score tracking feature.

If the user achieves a score higher than the previous high score and the game ends, the high score is updated and saved.

This project focuses on learning how to work with the file system, including reading from and writing to files.

Additionally, a Mail Merge mini project was completed to practice handling multiple files and automatically generating personalized letters.
---

### 📝 Tasks
- Add a high score tracking feature to the Snake Game.
- Save the highest score using a local text file.
- Read the saved high score when the game starts.
- Update the high score file when the player beats the previous record.
- Practice reading from and writing to files using Python.
- Complete a Mail Merge project using text files and directories.
- Automatically generate personalized invitation letters.

---

## 🧠 Notes

### Files System - Read
```python
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()
```
Why is file.close() necessary?

Because opened files use system resources, and closing the file properly prevents resource leaks and ensures changes are saved correctly.


Another way:
```python
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
```
Using `with open()` automatically closes the file after the block is finished.

### Files System - Write
```python
with open("my_file.txt", mode="w") as file:
   file.write("New Text")
```

Appending text without deleting existing content:
```python
file.write("\nNew Text")
```
If the file does not exist, Python automatically creates a new file with the given name and writes the string into it.

### File Paths
- Absolute Path:

An absolute path is the full path to a file or folder starting from the root directory.

Example:
```python
/Users/username/Desktop/my_file.txt
```
It always points to the same location no matter where the current project folder is.

- Relative Path:

A relative path is based on the current working directory.

Example:
```python
../../Desktop/my_file.txt
```
.. means moving up one folder level.

../../ means moving up two folder levels.

Relative paths are useful when sharing projects because they work as long as the project folder structure stays the same.

### .strip() Function
`.strip()` removes unnecessary whitespace characters from the beginning and end of a string.

This includes spaces, newline characters(`\n`) and tabs(`\t`)

Example:
```python
invited_names.txt
Angela
Jack
Sophie
```
Without `.strip()`
```python
with open("invited_names.txt") as file:
    for line in file:
        print(line)
```
Output:
```python
Angela

Jack

Sophie
```
Extra blank lines appear because the string already contains \n and print() also adds a new line automatically.

With `.strip()`
```python
with open("invited_names.txt") as file:
    for line in file:
        print(line.strip())
```
Output:
```python
Angela
Jack
Sophie
```

### .replace() Function
`.replace()` replaces a specific part of a string with another value.

Syntax:
```python
string.replace(old_value, new_value)
```
Example:
```python
text = "Hello [name]"
new_text = text.replace("[name]", "Angela")
print(new_text)
```
Output:
```python
Hello Angela
```