import unittest
import socket
from ipaddress import IPv4Network
from threading import Thread

def task_func(ip_range, port):
    """
    Scans a specified IP address range and checks if a specified port is open on each IP.
    The function returns a dictionary with IP addresses as keys and a boolean indicating
    the port's status (True if open, False otherwise).
    """
    open_ports = {}

    def check_port(ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((str(ip), port))
            open_ports[str(ip)] = True
        except socket.error:
            open_ports[str(ip)] = False
        finally:
            sock.close()

    threads = []

    for ip in IPv4Network(ip_range):
        thread = Thread(target=check_port, args=(ip,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return open_ports

class TestTaskFunc(unittest.TestCase):

    def test_valid_ip_range_and_port(self):
        result = task_func('192.168.1.0/30', 80)
        self.assertIsInstance(result, dict)
        self.assertGreaterEqual(len(result), 4)  # There are 4 IPs in this range.
        
    def test_invalid_ip_range(self):
        with self.assertRaises(ValueError):
            task_func('256.256.256.256/24', 80)

    def test_empty_ip_range(self):
        with self.assertRaises(ValueError):
            task_func('', 80)

    def test_invalid_port(self):
        with self.assertRaises(ValueError):
            task_func('192.168.1.0/24', 70000)  # Port numbers should be between 0-65535

    def test_port_check_results(self):
        result = task_func('127.0.0.1/32', 22)  # Check for SSH on localhost
        self.assertIn('127.0.0.1', result)
        self.assertTrue(result['127.0.0.1'])  # Port 22 should normally be open if SSH is running

if __name__ == '__main__':
    unittest.main()