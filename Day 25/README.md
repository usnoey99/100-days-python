## Day 25 - Working with CSV Files and Analysing Data with Pandas

---

### 📌 Overview
pandas is one of the most popular Python libraries. In this lesson, we will learn how to use it to understand and analyse data efficiently.

By the end, we will create a game where you guess all the U.S. states and learn their locations. This game is inspired by the "States Game."

---

## 🧠 Notes

`pandas` is an open-source Python library that provides high-performance, easy-to-use data structures and data analysis tools. It’s especially popular for working with tabular data, like spreadsheets or SQL tables.
- Efficient handling of large datasets.
- Powerful data cleaning and transformation capabilities.
- Tools for time series analysis.
- Easy integration with other Python libraries like NumPy.

### Reading Files with Pandas
```python
import pandas as pd
data = pd.read_csv('data.csv')  # Read CSV file
```
- Each row in the CSV becomes a row in a DataFrame.
- Each column has a label and can be accessed individually.

### a Series in pandas
A `Series` in pandas is essentially a ont-dimensional labeled array that can hold data type.
- It acts like a NumPy array but with labels (index).
- Can store numbers, strings, or even Python objects.
- Supports vectorized operations and easy data manipulation.

Example:
```python
import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
```
Output:
```
a    10
b    20
c    30
dtype: int64
```

### Using Series in a Game
In our U.S. States game:
- Each state’s data (name, x-coordinate, y-coordinate) is stored in a CSV.
- When the user guesses a state, we filter the CSV using a pandas Series:
```python
state_data = data_set[data_set.state.str.lower() == answer_state.lower()]
x = int(state_data.x.values[0])
y = int(state_data.y.values[0])
```
This allows us to place the state name at the correct position on a map using Turtle.