import os
import unittest
from flask import Flask
from flask_mail import Mail

def task_func(app_name):
    app = Flask(app_name)
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'localhost')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 25))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', False) == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', None)
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', None)
    
    mail = Mail(app)
    
    return mail, {
        'MAIL_SERVER': app.config['MAIL_SERVER'],
        'MAIL_PORT': app.config['MAIL_PORT'],
        'MAIL_USE_TLS': app.config['MAIL_USE_TLS'],
        'MAIL_USERNAME': app.config['MAIL_USERNAME'],
        'MAIL_PASSWORD': app.config['MAIL_PASSWORD']
    }

class TestTaskFunc(unittest.TestCase):

    def test_mail_instance_creation(self):
        mail, configs = task_func("test_app")
        self.assertIsInstance(mail, Mail)

    def test_default_mail_server(self):
        mail, configs = task_func("test_app")
        self.assertEqual(configs['MAIL_SERVER'], 'localhost')

    def test_default_mail_port(self):
        mail, configs = task_func("test_app")
        self.assertEqual(configs['MAIL_PORT'], 25)

    def test_mail_use_tls_default(self):
        mail, configs = task_func("test_app")
        self.assertFalse(configs['MAIL_USE_TLS'])

    def test_app_name_configuration(self):
        mail, configs = task_func("my_flask_app")
        self.assertEqual(mail.app.name, "my_flask_app")

if __name__ == '__main__':
    unittest.main()