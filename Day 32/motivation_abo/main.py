import random
import smtplib
import datetime as dt

MY_EMAIL = "example@example.com"
MY_PASSWORD = "example.password"

today = dt.datetime.now
day_of_week = today.weekday() # index 0 = Monday

if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.example.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL,
                            msg="Subject: Monday Motivation"
                                f"\n\n{quote}"
                            )