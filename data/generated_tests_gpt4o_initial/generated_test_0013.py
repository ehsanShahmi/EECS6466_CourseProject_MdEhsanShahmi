import unittest
from unittest.mock import patch, MagicMock

class TestFTPFunctions(unittest.TestCase):

    @patch('ftplib.FTP')
    def test_successful_connection(self, mock_ftp):
        mock_ftp.return_value.login = MagicMock()
        mock_ftp.return_value.cwd = MagicMock()
        mock_ftp.return_value.nlst.return_value = ['file1.txt', 'file2.txt']
        
        from your_module import task_func  # Replace 'your_module' with the actual module name
        result = task_func()
        
        self.assertEqual(result, ['file1.txt', 'file2.txt'])
        mock_ftp.assert_called_with('ftp.dlptest.com')

    @patch('ftplib.FTP')
    def test_connection_failure(self, mock_ftp):
        mock_ftp.side_effect = Exception("Connection failed")
        
        from your_module import task_func  # Replace 'your_module' with the actual module name
        
        with self.assertRaises(Exception) as context:
            task_func()
        self.assertEqual(str(context.exception), 'Failed to connect to FTP server ftp.dlptest.com: Connection failed')

    @patch('ftplib.FTP')
    def test_login_failure(self, mock_ftp):
        mock_ftp_instance = mock_ftp.return_value
        mock_ftp_instance.login.side_effect = Exception("Login failed")
        
        from your_module import task_func  # Replace 'your_module' with the actual module name
        
        with self.assertRaises(Exception) as context:
            task_func()
        self.assertEqual(str(context.exception), 'Failed to log into FTP server ftp.dlptest.com with user dlpuser: Login failed')

    @patch('ftplib.FTP')
    def test_directory_change_failure(self, mock_ftp):
        mock_ftp_instance = mock_ftp.return_value
        mock_ftp_instance.login = MagicMock()
        mock_ftp_instance.cwd.side_effect = Exception("Directory change failed")
        
        from your_module import task_func  # Replace 'your_module' with the actual module name
        
        with self.assertRaises(Exception) as context:
            task_func()
        self.assertEqual(str(context.exception), 'Failed to change to directory /ftp/test on server ftp.dlptest.com: Directory change failed')

    @patch('os.makedirs')
    @patch('subprocess.call')
    @patch('ftplib.FTP')
    def test_file_downloads(self, mock_ftp, mock_subprocess, mock_makedirs):
        mock_ftp_instance = mock_ftp.return_value
        mock_ftp_instance.login = MagicMock()
        mock_ftp_instance.cwd = MagicMock()
        mock_ftp_instance.nlst.return_value = ['file1.txt', 'file2.txt']
        
        from your_module import task_func  # Replace 'your_module' with the actual module name
        result = task_func()
        
        self.assertEqual(result, ['file1.txt', 'file2.txt'])
        self.assertTrue(mock_makedirs.called)
        self.assertEqual(mock_subprocess.call.call_count, 2)  # We expect two downloads
        

if __name__ == '__main__':
    unittest.main()