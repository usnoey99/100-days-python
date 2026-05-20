## Day 26 - List and Dictionary Comprehensions

---

### 📌 Overview
Learned the syntax and usage of list and dictionary comprehensions in Python.
Finally applied these concepts in a project that converts user-input words into a NATO phonetic alphabet list.

---

### 📝 Tasks
- Create lists using list comprehension
- Filter lists using conditions
- Create dictionaries using dictionary comprehension
- Read CSV data and convert it into a dictionary
- Build a NATO Alphabet converter project

---

## 🧠 Notes

### List Comprehension
A concise way to create lists in Python using a single line of code.
- Syntax:
    ```python
    new_list = [new_item for item in list]
    ```
    Example:
    ```python
    numbers = [1, 2, 3, 4, 5]
    squares = [x * x for x in numbers]
    print(squares)
    ```
    Output:
    ```python
    [1, 4, 9, 16, 25]
    ```
    
- Using if:
    ```python
    [expression for item in iterable if condition]
    ```
    Example: keep only even numbers
    ```python
    numbers = [1, 2, 3, 4, 5, 6]
    evens = [x for x in numbers if x % 2 == 0]
    print(evens)
    ```
    Output:
    ```python
    [2, 4, 6]
    ```
    
- Using if-else:
    ```python
    [value_if_true if condition else value_if_false for item in iterable]
    ```
    Example:
    ```python
    numbers = [1, 2, 3, 4]
    result = ["even" if x % 2 == 0 else "odd" for x in numbers]
    print(result)
    ```
    Output:
    ```python
    ['odd', 'even', 'odd', 'even']
    ```

- Comparison with a Regular for Loop
    Regular loop:
    ```python
    result = []
    for x in range(5):
    result.append(x * 2)
    ```
    List comprehension:
    ```python
    result = [x * 2 for x in range(5)]
    ```

- Nested Loops
    Example:
    ```python
    pairs = [(x, y) for x in range(3) for y in range(2)]
    print(pairs)
    ```
    Output:
    ```python
    [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    ```

### Dictionary Comprehension
A concise way to create dictionaries in Python.

- Syntax:
    ```python
    new_dict = {new_key:new_value for item in iterable}
    ```
    Example:
    ```python
    squares = {x: x * x for x in range(5)}
    print(squares)
    ```
    Output:
    ```python
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    ```
  
- Convert List to Dictionary
    ```python
    words = ["apple", "banana", "cherry"]
    lengths = {word: len(word) for word in words}
    print(lengths)
    ```
    Output:
    ```python
    {
        'apple': 5,
        'banana': 6,
        'cherry': 6
    }
    ```

- Swap Keys and Values
    ```python
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {value: key for (key, value) in original.items()}
    print(swapped)
    ```
    Output:
    ```python
    {1: 'a', 2: 'b', 3: 'c'}
    ```

### DataFrame `.iterrows()` looping
Iterates through DataFrame row by row.
```python
import pandas as pd
data = {
    "product": ["apple", "banana", "orange"],
    "price": [1000, 500, 800]
}
df = pd.DataFrame(data)
for index, row in df.iterrows():
    print(row.product, row.price)
```
- useful for row-by-row processing
- can be used with conditions and calculations

### Dictionary Comprehension with DataFrame
Dictionary Comprehension with DataFrame

Syntax:
```python
{row.column_name: row.other_column for index, row in dataframe.iterrows()}
```
Example:
```python
{row.name: row.score for index, row in student_data_frame.iterrows()}
```
How it works:
```python
for index, row in df.iterrows():
    key = row.name
    value = row.score
    dictionary[key] = value
```
- `iterrows()` returns `(index, row)`
- `row` is a pandas *Series* representing one row of the DataFrame
- values are accessed using `row.column_name`