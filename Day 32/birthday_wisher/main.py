import datetime as dt
import smtplib
from random import choice

my_email = ""
password = ""

def send_email(email):
    """Send email"""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="pythonmaster2023@yahoo.com", msg=email)


def get_quote():
    """Return's random quote from quotes.txt"""
    with open("./quotes.txt") as quotes:
        quotes_list = quotes.readlines()
    return choice(quotes_list)

def check_day():
    """Check if day is thursday"""
    current_day = dt.datetime.now().weekday()
    if current_day == 3:
        return True
    else:
        return False


if check_day():
    email_to_send = f"Subject: Quote of the day\n\n{get_quote()}"
    send_email(email_to_send)
else:
    print("Today is not thursday")