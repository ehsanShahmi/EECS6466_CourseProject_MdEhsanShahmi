import os
import unittest
from flask import Flask
from flask_mail import Mail

# Here is your prompt:
import os
from flask_mail import Mail

def task_func(app):
    """
    Initialize a Flask application with Flask-Mail. 

    Parameters:
    app (Flask): The Flask application to configure.

    Returns:
    tuple: A tuple containing the Flask-Mail instance and the app's mail configurations.

    Note:
    - The details of the email server are retrieved from environment variables. 
    - If the variables do not exist, use defaults.
    
    Requirements:
    - os
    - flask_mail

    Example:
    >>> from flask import Flask
    >>> app = Flask("test")
    >>> mail, configs = task_func(app)
    >>> 'MAIL_SERVER' in configs
    True
    """

           
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
    
    def setUp(self):
        """Create a Flask application for testing."""
        self.app = Flask("test")

    def test_default_mail_server(self):
        """Test default MAIL_SERVER value."""
        mail, configs = task_func(self.app)
        self.assertEqual(configs['MAIL_SERVER'], 'localhost')

    def test_default_mail_port(self):
        """Test default MAIL_PORT value."""
        mail, configs = task_func(self.app)
        self.assertEqual(configs['MAIL_PORT'], 25)

    def test_default_mail_use_tls(self):
        """Test default MAIL_USE_TLS value."""
        mail, configs = task_func(self.app)
        self.assertFalse(configs['MAIL_USE_TLS'])

    def test_mail_username_and_password_are_none_by_default(self):
        """Test that MAIL_USERNAME and MAIL_PASSWORD are None by default."""
        mail, configs = task_func(self.app)
        self.assertIsNone(configs['MAIL_USERNAME'])
        self.assertIsNone(configs['MAIL_PASSWORD'])

    def test_mail_instance_created(self):
        """Test that a Mail instance is created."""
        mail, configs = task_func(self.app)
        self.assertIsInstance(mail, Mail)

if __name__ == '__main__':
    unittest.main()