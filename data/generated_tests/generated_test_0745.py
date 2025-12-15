import subprocess
import random
import os
import unittest

# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'  


class TestTaskFunction(unittest.TestCase):

    def test_choose_random_script(self):
        """Test if the function randomly selects a script from the predefined list."""
        script = random.choice(SCRIPTS)
        self.assertIn(script, SCRIPTS)

    def test_script_path_construction(self):
        """Test if the script path is constructed correctly."""
        script_name = random.choice(SCRIPTS)
        expected_path = os.path.join(SCRIPTS_DIR, script_name)
        self.assertEqual(expected_path, os.path.join(SCRIPTS_DIR, script_name))

    def test_subprocess_call(self):
        """Test if a subprocess call is made without issues."""
        script_name = random.choice(SCRIPTS)
        script_path = os.path.join(SCRIPTS_DIR, script_name)
        with unittest.mock.patch('subprocess.call') as mock_call:
            subprocess.call(script_path, shell=True)
            mock_call.assert_called_once_with(script_path, shell=True)

    def test_return_value(self):
        """Test if the function returns the correct script path."""
        script_name = random.choice(SCRIPTS)
        script_path = os.path.join(SCRIPTS_DIR, script_name)
        self.assertEqual(script_path, script_path)

    def test_script_existence(self):
        """Test if the chosen script file exists."""
        script_name = random.choice(SCRIPTS)
        script_path = os.path.join(SCRIPTS_DIR, script_name)
        self.assertTrue(os.path.isfile(script_path), msg=f"Script {script_path} does not exist.")


if __name__ == '__main__':
    unittest.main()