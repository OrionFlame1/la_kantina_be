from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aditoma123@gmail.com'
app.config['MAIL_PASSWORD'] = 'dtbv jqfw pdbx fviq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/sendmail')
def send_mail():
    msg = Message('Hello aditios', sender='aditoma123@gmail.com', recipients=['aditoma123@yahoo.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return 'Message sent!'


if __name__ == '__main__':
    app.run(debug = True)
