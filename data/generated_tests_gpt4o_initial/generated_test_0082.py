import unittest
from flask import Flask
from flask_login import login_user
from wtforms.forms import ValidationError
from your_module import task_func, LoginForm  # Replace 'your_module' with the actual module name where task_func is defined

class TestLoginForm(unittest.TestCase):

    def setUp(self):
        self.form = LoginForm()

    def test_username_field_validation(self):
        self.form.username.data = 'testuser'
        self.assertTrue(self.form.validate(), "Username should be valid")
    
    def test_username_too_short(self):
        self.form.username.data = 'abc'
        self.assertFalse(self.form.validate(), "Username should be at least 4 characters long")
        self.assertIn('This field requires at least 4 characters.', self.form.username.errors)
    
    def test_username_too_long(self):
        self.form.username.data = 'a' * 26
        self.assertFalse(self.form.validate(), "Username should be at most 25 characters long")
        self.assertIn('This field can be at most 25 characters long.', self.form.username.errors)

    def test_password_field_validation(self):
        self.form.password.data = 'strongpassword'
        self.assertTrue(self.form.validate(), "Password should be valid")
    
    def test_password_too_short(self):
        self.form.password.data = 'short'
        self.assertFalse(self.form.validate(), "Password should be at least 8 characters long")
        self.assertIn('This field requires at least 8 characters.', self.form.password.errors)
    
    def test_password_too_long(self):
        self.form.password.data = 'a' * 81
        self.assertFalse(self.form.validate(), "Password should be at most 80 characters long")
        self.assertIn('This field can be at most 80 characters long.', self.form.password.errors)

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = task_func('mysecretkey', 'templates')
        self.client = self.app.test_client()

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_protected_route_redirects(self):
        response = self.client.get('/protected', follow_redirects=True)
        self.assertIn(b'Log In', response.data)  # Check if login page is displayed

    def test_login_success(self):
        with self.client:
            response = self.client.post('/login', data={'username': 'testuser', 'password': 'strongpassword'})
            self.assertEqual(response.status_code, 302)  # Check for redirect
            self.assertIn(b'Logged in as:', response.data)

if __name__ == '__main__':
    unittest.main()