import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from controller.UserController import UserController
from controller.ReservationController import ReservationController


class FlaskApp:
    def __init__(self, app_name, **configs):
        self.app = Flask(app_name)
        self.configs(**configs)
        self.setup_routes()
        CORS(self.app, supports_credentials=True)
        self.app.session = {}
        self.app.run(debug=(os.getenv("ENVIRONMENT") != "PRODUCTION"), host="0.0.0.0", port=5000)

    def configs(self):
        self.app.config.update(
            SESSION_COOKIE_SECURE=True,
            SESSION_COOKIE_HTTPONLY=True,
            SESSION_COOKIE_SAMESITE='None',
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PORT=465,
            MAIL_USERNAME='aditoma123@gmail.com',
            MAIL_PASSWORD='dtbv jqfw pdbx fviq',
            MAIL_USE_TLS=False,
            MAIL_USE_SSL=True
        )

    def setup_routes(self):
        self.app.add_url_rule('/login', 'login', self.login, methods=['POST'])
        # self.app.add_url_rule('/register', 'register', self.register)

        self.app.add_url_rule('/reservations', 'reservations', self.reservations, methods=['GET'])
        self.app.add_url_rule('/reservations/make', 'reservations_make', self.reservations_make, methods=['POST'])
        # self.app.add_url_rule('/reservations/confirm/<reservation_id>', 'res_confirm', self.reservations_confirm)
        self.app.add_url_rule('/reservations/cancel/<reservation_id>', 'res_cancel', self.reservations_cancel, methods=['POST'])
        self.app.add_url_rule('/reservations/confirm_arrival/<reservation_id>', 'res_confirm_arrival', self.reservations_confirm_arrival, methods=['POST'])
        self.app.add_url_rule('/reservations/complete/<reservation_id>', 'res_complete', self.reservations_complete, methods=['POST'])
        self.app.add_url_rule('/test_mail', 'test_mail', self.test_mail,  methods=['POST'])

    def test_mail(self):
        data = request.get_json()
        UserController.sendMail(data)
        return jsonify({
            'message': 'Mail sent'
        })

    """
    {
    "email": "adi@company.com",
    "password": "admin1"
    }
    """
    def login(self):
        data = request.get_json()
        login_status = UserController.login(data)
        if isinstance(login_status, int):
            self.app.session['user_id'] = login_status
            resp = make_response(
                jsonify(
                    {
                        'user_id': login_status
                    }
                )
            )
            resp.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'
        else:
            resp = jsonify({
                'message': login_status
            })
        return resp


    def reservations(self):
        if 'user_id' in self.app.session:
            reservations = ReservationController.getReservations()
            return jsonify({
                'reservations': reservations
            })
        else:
            return jsonify({
                'message': 'You are not logged in'
            })



    def reservations_make(self):
        if 'user_id' in self.app.session:
            data = request.get_json()
            reservation = ReservationController.createReservation(data)
            return jsonify({
                'reservation': reservation
            })
        else:
            return jsonify({
                'message': 'You are not logged in'
            })

    def reservations_cancel(self, reservation_id):
        if 'user_id' in self.app.session:
            reservation = ReservationController.cancelReservation(reservation_id)
            return jsonify({
                'reservation': reservation
            })
        else:
            return jsonify({
                'message': 'You are not logged in'
            })

    def reservations_confirm_arrival(self, reservation_id):
        if 'user_id' in self.app.session:
            reservation = ReservationController.confirmArrival(reservation_id)
            return jsonify({
                'reservation': reservation
            })
        else:
            return jsonify({
                'message': 'You are not logged in'
            })

    def reservations_complete(self, reservation_id):
        if 'user_id' in self.app.session:
            reservation = ReservationController.completeReservation(reservation_id)
            return jsonify({
                'reservation': reservation
            })
        else:
            return jsonify({
                'message': 'You are not logged in'
            })


if __name__ == '__main__':
    load_dotenv()
    app_name = "La Kantina"
    flask_app = FlaskApp(__name__)


# load_dotenv()
# app = Flask(__name__)
# mail = Mail(app)
#
# app.config.update(
#     SESSION_COOKIE_SECURE=True,
#     SESSION_COOKIE_HTTPONLY=True,
#     SESSION_COOKIE_SAMESITE='None',
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT = 465,
#     MAIL_USERNAME = 'aditoma123@gmail.com',
#     MAIL_PASSWORD = 'dtbv jqfw pdbx fviq',
#     MAIL_USE_TLS = False,
#     MAIL_USE_SSL = True
# )
# CORS(app, supports_credentials=True)
#
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'aditoma123@gmail.com'
# app.config['MAIL_PASSWORD'] = 'dtbv jqfw pdbx fviq'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
#
# mydb = db.init_db()
#
# # Set a secret key for session management
# app.secret_key = os.getenv("SESSION_SECRET")
#
#
# @app.route('/')
# def index():
#     return redirect('/login')
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data['email']
#     password = data['password']
#
#     user = validateLoginData(email, password)
#     if user:
#         session['user_id'] = user[0]
#         resp = make_response(
#             jsonify(
#                 {
#                     'status': 'success',
#                     'id': user[0],
#                     'name': user[1],
#                     'email': user[2],
#                     'type': user[4],
#                     'points': user[5]
#                 }
#             )
#         )
#         resp.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'
#         return resp
#     else:
#         return jsonify({
#             'status': 'failed'
#         })
#
#
# @app.route('/register', methods=['POST'])
# def register():
#     send_mail()
#     msg = Message('Hello aditios', sender='aditoma123@gmail.com', recipients=['aditoma123@yahoo.com'])
#     msg.body = "Hello Flask message sent from Flask-Mail"
#     mail.send(msg)
#     return 'Message sent!'
#
#
# @app.route('/tables', methods=['GET'])
# def tables():
#     return 'tables lmao'
#
#
# if __name__ == '__main__':
#     app.run()
