## Day 37 - Advanced Authentication and POST / PUT / DELETE Requests

---

### 📌 Overview
Using the Pixela API to build a habit tracker that records daily activities as graphs. Learned how to authenticate requests using HTTP headers and tokens, create new data with POST requests, update existing data with PUT requests, and remove data with DELETE requests.

---

### 📝 Tasks
- Create a Pixela user account through the API
- Create a graph for tracking daily habits
- Add new data points (pixels) to a graph
- Update existing data using a PUT request
- Delete data using a DELETE request
- Authenticate API requests using HTTP headers
- Automatically generate dates using `strftime()`

---

## 🧠 Notes

### HTTP Requests
HTTP requests allow a client to communicate with a server and perform different actions on data.

- POST Request: Creates new data on the server.
Example:
```python
new_data = {
    "date": "2026-06-10",
    "quantity": "10"
}
response = requests.post(url, json=new_data)
```

- PUT Request: Updates existing data on the server.
Example:
```python
updated_data = {
    "quantity": "15"
}
response = requests.put(url, json=updated_data)
```

- DELETE Request: Removes existing data from the server.
```python
response = requests.delete(url)
```

### HTTP Headers
HTTP headers are additional pieces of information sent along with an HTTP request or response.

They are commonly used to:
- Provide authentication credentials
- Specify the content type of the request
- Send additional metadata to the server

Example:
```python
headers = {
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)
```

### Advanced Authentication with HTTP Headers
Many modern APIs use HTTP headers for authentication instead of passing API keys in URL parameters.

A common approach is to include an authentication token in the `Authorization` header.

Example:
```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
    # `Bearer` indicates the authentication scheme.
    # `YOUR_TOKEN` is the access token provided by the API server.
}
response = requests.get(url, headers=headers)
```
- Keeps sensitive credentials out of the URL
- More secure than exposing APU keys in query parameters
- Widely used by modern REST APIs

### Authorization Header vs API Key
API Key in URL Parameters:
```python
params = {
    "apikey": "YOUR_API_KEY"
}
response = requests.get(url, params=params)
```
Token in HTTP Headers:
```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
response = requests.get(url, headers=headers)
```
The header-based approach is generally preferred because credentials are separated from the URL and are less likely to be exposed in logs or browser history.

### Generating Dates with strftime()
The `strftime()` method converts a `datetime` object into a formatted string.

Pixela requires dates in the format YYYYMMDD.

Example:
```
from datetime import datetime
today = datetime.now().strftime("%Y%m%d")
print(today)
```
Output:
```
20260610
```
This allows dates to be generated automatically instead of being entered manually each day.