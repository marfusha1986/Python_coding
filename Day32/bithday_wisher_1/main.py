import datetime  as dt
import pandas
import random
import smtplib
##################### Normal Starting Project ######################
my_email = 'marfushamarfusha1988@gmail.com'
password = 'hm410542HM!'
now = dt.datetime.now()
birthday_day = now.day
birthday_month = now.month
birthday_tuple = (birthday_month,birthday_day)
birthday_file = pandas.read_csv('birthdays.csv')

birthday_dict = {
    (birthday_file_row['month'],birthday_file_row['day']): birthday_file_row for (index,birthday_file_row) in birthday_file.iterrows()
}
if birthday_tuple in birthday_dict:
    birthday_person = birthday_dict[birthday_tuple]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as random_letter:
        content = random_letter.readline()
        content.replace('[NAME]',birthday_person['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f'Subject:Happy Birthday {birthday_person["name"]}\n\n{content}')
        connection.close()




