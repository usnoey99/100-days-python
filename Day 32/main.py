import smtplib

my_email = "yeonsuforexample@gmail.com"
my_password = "password2026"

# connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="yeonsuforexample@outlook.de",
                        msg="Subject: Test Email"
                            "\n\nHello Hello Hello")
# connection.close()

import datetime as dt

now = dt.datetime.now
year = now.year
month = now.month
day_of_week = now.weekday() # index 0 = Monday

date_of_birth = dt.datetime(1999, 12, 29)