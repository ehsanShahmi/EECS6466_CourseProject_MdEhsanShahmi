import unittest
from flask import Flask
from flask_mail import Mail

# Here is your prompt:
from flask import Flask
from flask_mail import Mail, Message

def task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder):
    """
    Creates a Flask application configured to send emails using Flask-Mail.
    It sets up the necessary SMTP configuration dynamically based on provided parameters
    and defines a route to send a test email.

    Parameters:
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        smtp_user (str): The SMTP username.
        smtp_password (str): The SMTP password.
        template_folder (str): The folder path for email templates.

    Requirements:
    - flask.Flask
    - flask_mail.Mail
    - flask_mail.Message

    Returns:
        Flask: A Flask application instance configured for sending emails.

    Examples:
    >>> app = task_func('smtp.example.com', 587, 'user@example.com', 'password', 'templates')
    >>> type(app).__name__
    'Flask'
    >>> app.config['MAIL_USERNAME'] == 'user@example.com'
    True
    """

    app = Flask(__name__, template_folder=template_folder)
    app.config['MAIL_SERVER'] = smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USERNAME'] = smtp_user
    app.config['MAIL_PASSWORD'] = smtp_password
    app.config['MAIL_USE_TLS'] = True
    
    mail = Mail()
    mail.init_app(app)

    @app.route('/send_mail')
    def send_mail():
        msg = Message('Hello', sender='from@example.com', recipients=['to@example.com'])
        msg.body = 'Hello Flask message sent from Flask-Mail'
        mail.send(msg)

        return 'Mail sent!'

    return app

class TestTaskFunc(unittest.TestCase):

    def test_create_app_instance(self):
        app = task_func('smtp.example.com', 587, 'user@example.com', 'password', 'templates')
        self.assertIsInstance(app, Flask)

    def test_app_configuration(self):
        app = task_func('smtp.example.com', 587, 'user@example.com', 'password', 'templates')
        self.assertEqual(app.config['MAIL_SERVER'], 'smtp.example.com')
        self.assertEqual(app.config['MAIL_PORT'], 587)
        self.assertEqual(app.config['MAIL_USERNAME'], 'user@example.com')
        self.assertEqual(app.config['MAIL_PASSWORD'], 'password') 
        self.assertTrue(app.config['MAIL_USE_TLS'])

    def test_template_folder(self):
        template_folder = 'templates'
        app = task_func('smtp.example.com', 587, 'user@example.com', 'password', template_folder)
        self.assertEqual(app.template_folder, template_folder)

    def test_mail_sending_route(self):
        app = task_func('smtp.example.com', 587, 'user@example.com', 'password', 'templates')
        with app.test_client() as client:
            response = client.get('/send_mail')
            self.assertEqual(response.data.decode('utf-8'), 'Mail sent!')

    def test_app_has_mail_instance(self):
        app = task_func('smtp.example.com', 587, 'user@example.com', 'password', 'templates')
        self.assertIsInstance(app.extensions['mail'], Mail)

if __name__ == '__main__':
    unittest.main()