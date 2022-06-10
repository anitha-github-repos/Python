
import smtplib
import datetime
import random

my_email = "practiceforpython30@gmail.com"
#my_yahoo_mail = "practiceforpython@yahoo.com"
my_password = "oaffoziqzxojnkfh"
#my_password_yahoo = "cvmuqnihgrazctko"

#smtp.gmail.com"


date = datetime.datetime.now()

if date.weekday() == 0:
    with open("quotes.txt", "r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="practiceforpython@yahoo.com",
                            msg=f"Subject:Hello\n\n{quote}")


# import datetime
#
# now = datetime.datetime.now()
#
# now.year