import unittest
from django.http import HttpResponse
import json
import random
import time

# Here is your prompt:
# 
# from django.http import HttpResponse
# from django.conf import settings
# import random
# import time
# 
# def task_func(data, min_delay, max_delay):
#     """
#     After a random delay, generate a Django HttpResponse with JSON data to simulate the latency of the network.
#     
#     Parameters:
#     data (str): The data to be included in the response body.
#     min_delay (int): The minimum delay in seconds.
#     max_delay (int): The maximum delay in seconds.
#     
#     Returns:
#     HttpResponse: A Django HttpResponse with JSON data.
#     
#     Requirements:
#     - django
#     - random
#     - time
# 
#     Example:
#     >>> import json
#     >>> random.seed(0)
#     >>> response = task_func(json.dumps({"Sample-Key": "Sample-Value"}), 1, 5)
#     >>> response.status_code
#     200
#     >>> json.loads(response.content)
#     {"Sample-Key": "Sample-Value"}
#     """
# 
#     # Generate a random delay
#     delay = random.uniform(min_delay, max_delay)
# 
#     # Wait for the delay
#     time.sleep(delay)
# 
#     response = HttpResponse(data, content_type='application/json')
# 
#     return response

class TestTaskFunc(unittest.TestCase):

    def test_response_status_code(self):
        response = task_func(json.dumps({"key": "value"}), 1, 2)
        self.assertEqual(response.status_code, 200)

    def test_response_content_type(self):
        response = task_func(json.dumps({"key": "value"}), 1, 2)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_response_data(self):
        data = json.dumps({"key": "value"})
        response = task_func(data, 1, 2)
        self.assertEqual(json.loads(response.content), json.loads(data))

    def test_random_delay_within_bounds(self):
        min_delay = 1
        max_delay = 2
        start_time = time.time()
        task_func(json.dumps({"key": "value"}), min_delay, max_delay)
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.assertGreaterEqual(elapsed_time, min_delay)
        self.assertLessEqual(elapsed_time, max_delay)

    def test_empty_data(self):
        response = task_func(json.dumps({}), 1, 2)
        self.assertEqual(json.loads(response.content), {})


if __name__ == '__main__':
    unittest.main()