from flask import Flask, request, jsonify
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
        #
        self.app.add_url_rule('/reservations', 'reservations', self.reservations, methods=['GET'])
        # self.app.add_url_rule('/reservations/confirm/<reservation_id>', 'res_confirm', self.reservations_confirm)
        # self.app.add_url_rule('/reservations/cancel/<reservation_id>', 'res_cancel', self.reservations_cancel)
        # self.app.add_url_rule('/reservations/confirm_arrival/<reservation_id>', 'res_confirm_arrival', self.reservations_confirm_arrival)
        #
        # self.app.add_url_rule('/table/<id>', 'table', self.table)

    def login(self):
        data = request.get_json()
        login_status = UserController.login(data)
        user_id = login_status
        if user_id:
            self.app.session['user_id'] = user_id
        return jsonify(login_status)

        # email = data['email']
        # password = data['password']
        #
        # user = validateLoginData(email, password)
        # if user:
        #     session['user_id'] = user[0]
        #     resp = make_response(
        #         jsonify(
        #             {
        #                 'status': 'success',
        #                 'id': user[0],
        #                 'name': user[1],
        #                 'email': user[2],
        #                 'type': user[4],
        #                 'points': user[5]
        #             }
        #         )
        #     )
        #     resp.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'
        #     return resp
        # else:
        #     return jsonify({
        #         'status': 'failed'
        #     })

    def reservations(self):
        try:
            user_id = self.app.session['user_id']
            return jsonify({
                'status': 'success',
                'user_id': user_id
            })
        except:
            return jsonify({
                'status': 'failed'
            })


if __name__ == '__main__':
    app_name = "La Kantina"
    flask_app = FlaskApp(app_name)
    flask_app.app.run()


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
