import unittest
import subprocess
from multiprocessing import Pool

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output

def task_func(commands):
    """
    Executes a list of shell commands in parallel using multiprocessing, and collects their outputs.
    
    Parameters:
        commands (list): A list of shell commands to be executed.

    Returns:
        list: A list of byte strings, each representing the output of a command. Returns an empty list if `commands` is empty.

    Requirements:
    - subprocess
    - multiprocessing.Pool

    Notes:
    - If `commands` is an empty list, the function returns an empty list without attempting to execute any commands.
    
    Examples:
    >>> result = task_func(['ls', 'pwd', 'date'])
    >>> isinstance(result, list)
    True
    >>> all(isinstance(output, bytes) for output in result)
    True
    """

           
    if not commands:  # Handle case where commands list is empty
        return []

    with Pool(processes=len(commands)) as pool:
        outputs = pool.map(execute_command, commands)

    return outputs

class TestTaskFunc(unittest.TestCase):

    def test_empty_commands(self):
        """Test that an empty list of commands returns an empty list."""
        result = task_func([])
        self.assertEqual(result, [])

    def test_single_command(self):
        """Test executing a single valid command."""
        result = task_func(['echo Hello'])
        self.assertEqual(result[0].strip(), b'Hello')

    def test_multiple_commands(self):
        """Test executing multiple valid commands."""
        commands = ['echo First', 'echo Second', 'echo Third']
        expected_outputs = [b'First', b'Second', b'Third']
        result = task_func(commands)
        for idx, output in enumerate(result):
            self.assertEqual(output.strip(), expected_outputs[idx])

    def test_non_existent_command(self):
        """Test executing a non-existent command returns an error."""
        result = task_func(['nonexistent_command'])
        self.assertNotEqual(result[0], b'')  # Error output should not be empty

    def test_command_with_args(self):
        """Test executing a command with arguments."""
        result = task_func(['echo argument1 argument2'])
        self.assertEqual(result[0].strip(), b'argument1 argument2')

if __name__ == '__main__':
    unittest.main()