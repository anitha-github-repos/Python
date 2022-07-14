import smtplib
from flight_data import FlightData

my_email = "practiceforpython30@gmail.com"
my_password = "oaffoziqzxojnkfh"

class NotificationManager:

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            for email in emails:
                connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg= f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8'))
