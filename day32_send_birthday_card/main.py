# 2022/03/02
##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import smtplib
import random
import pandas

now = dt.datetime.now()
month = now.month
day = now.day
birthdays_data = pandas.read_csv('birthdays.csv')
birthday_list = birthdays_data.to_dict(orient='records')

for people_dict in birthday_list:
    if people_dict['month'] == month and people_dict['day'] == day:
        my_email = 'e1xuan73@yahoo.com'
        my_password = 'vhhguhosfkozswre'
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as letter_file:
            content = letter_file.read()
            content = content.replace('[NAME]', people_dict["name"])               
        with smtplib.SMTP('smtp.mail.yahoo.com') as connection:            
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=people_dict['email'],
                msg=f'Subject:Happy Birthday!\n\n{content}'
            )

        # print(f'{people_dict["name"]} it is your birth. your email is {people_dict["email"]}')

# print(month,day)