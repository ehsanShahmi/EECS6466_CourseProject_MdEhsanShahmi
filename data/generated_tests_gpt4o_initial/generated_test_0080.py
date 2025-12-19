import unittest
from flask import Flask
import json
import logging
from your_module import task_func  # Replace 'your_module' with the actual name of your module

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.template_folder = 'test_templates'
        self.app = task_func(self.template_folder)
        self.client = self.app.test_client()
        self.app.context().push()

    def test_create_app_instance(self):
        """Test if the task_func returns a Flask application instance."""
        self.assertIsInstance(self.app, Flask)

    def test_route_method_is_post(self):
        """Test if the root route accepts POST requests."""
        with self.app.test_request_context():
            self.assertIn('POST', self.app.url_map['/'].methods)

    def test_logging_of_post_data(self):
        """Test if incoming POST request data is logged correctly."""
        with self.app.test_request_context():
            with self.assertLogs('root', level='INFO') as log:
                post_data = {'key': 'value'}
                response = self.client.post('/', json=post_data)
                self.assertEqual(response.status_code, 200)
                self.assertIn(json.dumps(post_data), log.output[0])

    def test_template_rendering(self):
        """Test if the 'index.html' is rendered with the correct data."""
        post_data = {'key': 'value'}
        response = self.client.post('/', json=post_data)
        
        # Check if the response is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if the response data contains the posted JSON data
        self.assertIn('key', response.get_data(as_text=True))  # Adjust according to how template renders the data

    def test_template_folder_path(self):
        """Test if the app is created with the specified template folder."""
        self.assertEqual(self.app.template_folder, self.template_folder)

if __name__ == '__main__':
    unittest.main()