## Day 33 - Application Programming Interfaces

---

### 📌 Overview
Learning how to work with APIs in Python.

Using external APIs to retrieve real-time data and build an ISS (International Space Station) tracker. The program checks whether the ISS is currently above my location and whether it is dark outside. If both conditions are met, it automatically sends an email notification telling me to look up.

---

### 📝 Tasks
- Learn how APIs work and how to make requests in Python
- Retrieve real-time ISS location data from an API
- Retrieve sunrise and sunset times from an API
- Build an ISS overhead notifier
- Automatically send an email when the ISS is visible above my location

---

## 🧠 Notes

### Application Programming Interface (API)
An API is a set of commands, functions, protocols, and objects that programmers can use to create software or interact with an external system.

APIs allow different applications to communicate with each other exchange data without needing to know how the other system is implemented internally.

Example:
```python
import requests
response = requests.get("https://api.example.com/users")
print(response.json())
```

### API Endpoint
An API endpoint is a specific URL where an API can be accessed.

Each endpoint usually represents a particular resource or action.

Example:
```
https://api.example.com/users
```
- Base URL: https://api.example.com
- Endpoint: /users

### API Request
An API request is a message sent by a client to an API server asking for data or requesting an action.

A request typically contains:
- HTTP method (GET, POST, PUT, DELETE)
- Endpoint URL
- Headers
- Parameters
- Request body (optional)

Example:
```python
import requests
response = requests.get(
    "https://api.example.com/users",
    params={"id": 1}
)
print(response.json())
```

### API Response
An API response is the data returned by the server after processing an API request.

A response usually contains:
- Status coed
- Headers
- Response body

Example:
```python
{
    "id": 1,
    "name": "John"
}
```

Common status codes:
- 1xx → Hold on, something's happening. This is not final. 
- 2xx → Success. The request was completed successfully.
- 3xx → Redirection. Additional action is required to complete the request.
- 4xx → Client error. Something is wrong with the request.
- 5xx → Server error. The server failed to process the request.

### requests Module
The `requests` module is a popular Python library used for making HTTP requests.
It allows Python programs to communicate with web servers and APIs.

### raise_for_status()
This method checks whether the HTTP request was successful.

If the server returns an error status code, an exception is raised.

### API Parameters
Parameters are additional values sent with an API request to customize the response.

Example:
```python
parameters = {
    "lat": 51.507351,
    "lng": -0.127758,
    "formatted": 0
}
response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params=parameters
)
```
The `requests` library automatically converts the dictionary into URL query parameters.