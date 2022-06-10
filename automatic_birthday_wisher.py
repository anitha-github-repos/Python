##################### Normal Starting Project ######################
import datetime
import smtplib
import pandas
import random

my_email = "practiceforpython30@gmail.com"
my_password = "oaffoziqzxojnkfh"

today_date = datetime.datetime.now()
today_tuple = (today_date.month, today_date.day)



csv = pandas.read_csv("birthdays.csv")

dict = csv.to_dict()


birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in csv.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    filepath = f"letter_templates/letter_{random.randint(1,4)}.txt"
    with open(filepath) as file:
        contents = file.read()
        new_content = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{new_content}"
        )





