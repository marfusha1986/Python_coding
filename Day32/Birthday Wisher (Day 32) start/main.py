import smtplib
import datetime as dt
import random


my_email = 'marfushamarfusha1988@gmail.com'
password='pr7Duct!'

now = dt.datetime.now()
day = now.weekday()

if day == 3:
    with open('quotes.txt') as quote_file:
        messages = quote_file.readlines()
        message = random.choice(messages)
    print(message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f'Subject:{day} Motivation\n\n{message}')
        connection.close()



