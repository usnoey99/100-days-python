## Day 32 - Email SMTP and the datetime module

---

### 📌 Overview
Sending emails with Python. Using the `datetime` module to determine when emails should be sent.

Finally, building a tool that automatically sends birthday congratulation emails.


---

### 📝 Tasks
- Build a program that sends motivational quotes every Monday
- Automatically send birthday congratulation emails to friends on their birthdays

---

## 🧠 Notes

### smtplib
A module provided by Python’s standard library for sending emails.  
It connects to an SMTP (Simple Mail Transfer Protocol) server and provides functionality for sending emails.

Example:
```python
import smtplib
from email.mime.text import MIMEText

# Create the email body
msg = MIMEText("Hallo, this is a test mail.")

# Set email subject
msg["Subject"] = "Test"

# Sender email address
msg["From"] = "sender@example.com"

# Receiver email address
msg["To"] = "receiver@example.com"

# Connect to Gmail SMTP server using port 587
smtp = smtplib.SMTP("smtp.gmail.com", 587)

# Start TLS encryption for secure communication
smtp.starttls()

# Log in with email address and app password
smtp.login("sender@example.com", "App Password")

# Send the email message
smtp.send_message(msg)

# Close the SMTP connection
smtp.quit()
```

### Sending Attachments
```python
from email.message import EmailMessage

# Create EmailMessage object
msg = EmailMessage()

# Open file in binary read mode
with open("test.pdf", "rb") as f:
    data = f.read()

# Attach the file to the email
msg.add_attachment(
    data,
    maintype="application", # Main MIME type
    subtype="pdf", # File subtype
    filename="test.pdf"
)
```

### sendmail() vs send_message()
- sendmail(): A low-level method that requires manual string conversion.
```python
smtp.sendmail(from_addr, to_addrs, msg.as_string())
```
- send_message(): A more modern and convenient method. It automatically handles email formatting and is easier to use.
```python
smtp.send_message(msg)
```

### datetime Module
A module provided by Python’s standard library for working with dates and times.

It is commonly used for:
- Getting the current date and time
- Measuring time differences
- Formatting dates
- Scheduling tasks
- Automating email sending times

Example:
```python
from datetime import datetime

# Get current date and time
now = datetime.now()

# Print current date and time
print(now)
```
Example output:
```python
2026-05-26 14:30:15.123456
```
- datetime.today(): Returns the current local date and time.
- strftime(): Formats a date/time object into a readable string.
  ```python
  formatted_date = now.strftime("%Y-%m-%d")
  print(formatted_date) # 2026-05-26
  ```
- strptime(): Converts a string into a datetime object.
- weekday(): Returns the day of the week as an integer.
- timedelta(): Is used to calculate differences betweens dates and times.
  ```python
  future_date = now + timedelta(days=7)
  print(future_date)
  ```