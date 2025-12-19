import re
import smtplib
import unittest
from unittest.mock import MagicMock, patch

# Constants
TEXT = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
RECEPIENT_ADDRESS = "names@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(text=TEXT, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, recepient_address=RECEPIENT_ADDRESS, smtp=None):
    """
    Extract all names from a string that is not enclosed by square brackets and send the names in an email.

    Parameters:
    text (str): The text from which to extract names.
    smtp_server (str): The SMTP server to use for sending the email.
    smtp_port (int): The port to use for the SMTP server.
    email_address (str): The email address from which to send the email.
    email_password (str): The password for the email address.
    recepient_address (str): The recepient email adress.
    
    Returns:
    list: A list of extracted names.
    
    Note:
    - The message in the email is formatted in "Subject: Extracted Names\n\n" with the extracted name "\nJosie Smith\nMugsy Dog Smith".

    Requirements:
    - re
    - smtplib

    Example:
    >>> from unittest.mock import MagicMock
    >>> mock_smtp_instance = MagicMock()
    >>> mock_smtp = MagicMock(return_value=mock_smtp_instance)
    >>> task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]", smtp=mock_smtp)
    ['Josie Smith', 'Mugsy Dog Smith']
    """

    names = re.findall('(.*?)(?:\\[.*?\\]|$)', text)
    # Remove trailing spaces from each name and filter out empty strings
    names = [name.strip() for name in names if name != ""]
    
    message = 'Subject: Extracted Names\n\n' + '\n'.join(names)
    if smtp:
        server = smtp(smtp_server, smtp_port)
    else:
        server = smtplib.SMTP(smtp_server, smtp_port)
        
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recepient_address, message)
    server.quit()
    return names

class TestTaskFunction(unittest.TestCase):

    def test_extract_names_basic(self):
        result = task_func(text="Alice Johnson [123 MAIN ST]Bob Smith [456 SIDE ST]")
        self.assertEqual(result, ['Alice Johnson', 'Bob Smith'])

    def test_extract_names_no_brackets(self):
        result = task_func(text="Charlie Brown and Lucy Van Pelt")
        self.assertEqual(result, ['Charlie Brown and Lucy Van Pelt'])

    def test_extract_names_empty_input(self):
        result = task_func(text="")
        self.assertEqual(result, [])

    def test_extract_names_multiple_entries(self):
        result = task_func(text="John Doe [ADDRESS]Jane Doe [ADDRESS]Tom Brown [ADDRESS]")
        self.assertEqual(result, ['John Doe', 'Jane Doe', 'Tom Brown'])

    @patch('smtplib.SMTP')
    def test_email_sending(self, mock_smtp):
        mock_instance = mock_smtp.return_value
        task_func(text="Test Sender [ADDRESS]", smtp=mock_smtp)
        self.assertTrue(mock_instance.starttls.called)
        mock_instance.login.assert_called_with(EMAIL_ADDRESS, EMAIL_PASSWORD)
        mock_instance.sendmail.assert_called_with(EMAIL_ADDRESS, RECEPIENT_ADDRESS, 'Subject: Extracted Names\n\nTest Sender') 

if __name__ == '__main__':
    unittest.main()