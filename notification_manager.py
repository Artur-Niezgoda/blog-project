"""
Module that sends an email with the message from the form

Classes:
    NotificationManager

Methods:
    send_email(message)
        sends the message to the given email
"""

from environs import Env
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText


# Read environment variables from env file
env = Env()
env.read_env()


class NotificationManager:
    """Class that sends an email to a single given email address"""

    def __init__(self):
        """
        Constructor of the class
        Attributes:
            my_email (string): email address from which the email will be send (saved in .env file)
            password (string): password generated for the email address (saved in .env file)
            my_email (string): email address to which the email will be send (saved in .env file)
        """

        self.my_email = env("MY_EMAIL")
        self.password = env("PASSWORD_EMAIL")
        self.to_email = env("MY_EMAIL")

    def send_email(self, name: str, email: str, phone: str, message: str) -> None:
        """
        Function that sends an emai containing the message from the Contact form

        :param name: name
        :param email: email address
        :param phone: phone number in the form of string
        :param message: containing the message
        """

         # Create message container
        msg = MIMEMultipart('alternative')
        msg.set_charset('UTF-8')
        msg['Subject'] = "Contact Form"
        msg['From'] = email
        msg['To'] = self.to_email
        msg.attach(MIMEText(f"\n\n Name: {name} \n\n Email: {email} \n\n Phone: {phone} \n\n Message: {message}"))



        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.my_email, self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.to_email,
                msg=msg.as_string()
            )
        print("An email has been sent.")
