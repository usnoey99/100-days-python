# Day 73 - Data Visualisation with Matplotlib

---

## 📌 Overview
Learn how to visualise data and create charts using Matplotlib.  
Use Pandas to pivot, group, and manipulate data into the desired format, then create and customise line charts using timestamps and time-series data.


---

## 📝 Tasks
* Create and customise charts with Matplotlib.
* Group, pivot, and manipulate data with Pandas.
* Convert dates to datetime objects.
* Handle missing values.
* Plot and compare multiple time-series lines.
* Use rolling averages to identify trends.


---

## 🧠 Note

### Matplotlib
Matplotlib is a Python library used to visualise data and create different types of charts.
```python
import matplotlib.pyplot as plt
```


### pd.to_datetime()
converts strings into datetime objects.

```python
df["DATE"] = pd.to_datetime(df["DATE"])
```
This makes it easier to work with dates and time-series data.


### .pivot()
reshapes a DataFrame by turning values from a column into new columns.

```python
reshaped_df = df.pivot( index="DATE", columns="TAG", values="POSTS" )
```
After pivoting, each programming language becomes a separate column.  
This format makes it easier to create charts comparing different programming languages.


### Handling NaN Values
`NaN` represents missing data.
```python
reshaped_df.isna().values.any()
```
This checks whether there is at least one `NaN` value in the DataFrame.
```python
reshaped_df.fillna(0)
```
This replaces missing values with `0`.


### Creating Line Charts
Matplotlib's .plot() can be used to create line charts.
```python
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)
```
`reshaped_df.index` is used for the x-axis because the dates became the DataFrame index after using `.pivot()`.

Each `.plot()` call adds another line to the same chart.

* figsize: changes the size of the chart.
* xlabel(): sets the x-axis label.
* ylabel() → sets the y-axis label.
* xticks() / yticks(): changes the font size of tick labels.
* ylim(): sets the minimum and maximum values of the y-axis.

* plt.legend(): displays those names on the chart.


## Rolling Mean
`.rolling().mean()` calculates a moving average over a specific number of observations.
```python
java["POSTS"].rolling(6).mean()
```
This calculates a 6-month rolling average.

A rolling average smooths out short-term fluctuations, making long-term trends easier to see.

For example:
```
Original Data
100 → 200 → 150 → 300 → 250 → 400

6-month average
             → 233.3
```
As new data is added, the window moves forward and the average is recalculated.




