import smtplib

my_email = ""
password = ""

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# print("connected to smtp server")
# connection.starttls()
# print("Started tls")
# connection.login(user=my_email, password=password)
# print("logged in")
# connection.sendmail(from_addr=my_email,
#                     to_addrs="pythonmaster2023@yahoo.com",
#                     msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                     to_addrs="pythonmaster2023@yahoo.com",
                    msg="Subject:Hello\n\nThis is the body of my email.")