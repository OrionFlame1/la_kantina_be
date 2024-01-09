from flask_mail import Mail, Message
from dotenv import load_dotenv
import os


class MailService:
    def __init__(self, app):
        self.app = app
        self.mail = Mail(app)
        load_dotenv()

    def send(self, to, subject, template):
        msg = Message(
            subject,
            recipients=[to],
            html=template,
            sender=(os.getenv("MAIL_SENDER"), self.app.config['MAIL_USERNAME'])
        )
        self.mail.send(msg)
