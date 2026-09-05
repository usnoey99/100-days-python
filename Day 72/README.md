# Day 72 - Data Exploration with Pandas

---

## 📌 Overview
Explore college major and salary data using Pandas.  
Analyze starting salaries, earning potential, income risk, and salary differences between Business, STEM, and HASS majors.


---

## 📝 Tasks
* Explore and clean a Pandas DataFrame.
* Select columns, rows, and cells.
* Find maximum and minimum values.
* Sort and add columns.
* Group and compare data by categories.


---

## 🧠 Note

### DataFrame Exploration
Use the following methods to explore a DataFrame:
```python
df.head()
df.tail()
df.shape
df.columns
```
- .head() → View the first rows.
- .tail() → View the last rows.
- .shape → Check the number of rows and columns.
- .columns → Check the column names.


### Missing Values
Use .isna() to find missing values:
```python
df.isna()
```
Use .dropna() to remove rows containing missing values:
```python
clean_df = df.dropna()
```


### Selecting Columns
Use [] to select columns:
```python
df["Major"]
```
Multiple columns can be selected using:
```python
df[["Major", "Starting Median Salary"]]
```

### Selecting Individual Cells
A specific cell can be accessed using:
```python
df["Major"][0]
```
or:
```python
df["Major"].loc[0]
```


### Finding Maximum and Minimum Values
Use the following methods to find maximum and minimum values:
```python
df["Starting Median Salary"].max()
df["Starting Median Salary"].min()
```
To find the index of the maximum or minimum value:
```python
df["Starting Median Salary"].idxmax()
df["Starting Median Salary"].idxmin()
```


### Sorting Data
Use .sort_values() to sort the DataFrame:
```python
df.sort_values("Starting Median Salary")
```
To sort from highest to lowest:
```python
df.sort_values("Starting Median Salary", ascending=False)
```


### Adding Columns
Use .insert() to add a new column at a specific position:
```python
df.insert(1, "New Column", values)
```


### Grouping Data
Use .groupby() to group data by categories and calculate statistics.  

For example, to calculate the average salary for each group:
```python
clean_df.groupby("Group").mean(numeric_only=True)
```
We can also specify a particular column:
```python
clean_df.groupby("Group")["Starting Median Salary"].mean()
```
This allows us to compare salary data across categories such as:
```text
Business
STEM
HASS
```