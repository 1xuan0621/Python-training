from calendar import weekday
import smtplib
import datetime as dt
import random


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open('quotes.txt') as data:
        quites_list = data.readlines()
        today_quote = random.choice(quites_list)
    
    my_email = 'e1xuan73@yahoo.com'
    password = 'vhhguhosfkozswre'
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='1xuan73e@gmail.com',
            msg=f'Subject:Hello\n\n{today_quote}'
        )

with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as letter_data:
    print(letter_data.read())