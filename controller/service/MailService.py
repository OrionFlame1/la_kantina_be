from flask_mail import Mail, Message
from dotenv import load_dotenv
import os


class MailService:
    def __init__(self, app):
        self.app = app
        self.mail = Mail(app)
        load_dotenv()

    def send(self, to, subject, body):
        msg = Message(
            subject,
            recipients=[to],
            body=body,
            sender=(self.app.config['MAIL_USERNAME'])
        )
        self.mail.send(msg)

    def sendAccountConfirmation(self, to, link):
        msg = Message(
            "Account Confirmation",
            recipients=[to],
            html=f"<h1>Click <a href='{link}'>here</a> to confirm your account</h1>",
            sender=(self.app.config['MAIL_USERNAME'])
        )
        self.mail.send(msg)

    def sendReservationConfirmation(self, to, link):
        msg = Message(
            "Reservation Confirmation",
            recipients=[to],
            html=f"<h1>Click <a href='{link}'>here</a> to confirm your reservation</h1>",
            sender=(self.app.config['MAIL_USERNAME'])
        )
        self.mail.send(msg)