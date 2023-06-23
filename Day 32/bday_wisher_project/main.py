
import smtplib
import random
import datetime as dt
import pandas

USERNAME = ""
PASSWORD = ""
# TODO 1: Get current day and month from datetime library
now = dt.datetime.now()
today = (now.month, now.day)


# TODO 2: Get data from birthdays.csv using pandas
birthdays = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row.get("month"), data_row.get("day")):data_row for (index, data_row) in birthdays.iterrows()}
# TODO 3: Check if birthday matches a day in dictionary
if today in birthdays_dict:
    birthday = birthdays_dict.get(today)
    # TODO 4: Pick random letter from letter_templates
    letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    letter = random.choice(letter_templates)
    with open(f"./letter_templates/{letter}") as letter_to_send:
        formatted_letter = f"Subject: Happy Birthday!\n\n{letter_to_send.read().replace('[NAME]', birthdays_dict.get(today).get('name'))}"
    # TODO 5: Send Happy Birthday email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs=birthday.get("email"), msg=formatted_letter)