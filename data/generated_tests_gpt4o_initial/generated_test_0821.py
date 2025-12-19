import time
import threading
import unittest

def task_func(delay_time: float = 1.0, num_threads: int = 5):
    results = []
    
    def delay():
        time.sleep(delay_time)
        results.append(f'Delay in thread {threading.current_thread().name} completed')

    for i in range(num_threads):
        t = threading.Thread(target=delay, name=str(i))
        t.start()
        t.join()  # Ensure that the thread completes before moving to the next

    return results

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        expected_output = [
            'Delay in thread 0 completed',
            'Delay in thread 1 completed',
            'Delay in thread 2 completed',
            'Delay in thread 3 completed',
            'Delay in thread 4 completed',
        ]
        output = task_func()
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_custom_delay_time(self):
        start_time = time.time()
        output = task_func(0.2, 3)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1.0)  # Should complete within reasonable time
        
        expected_output = [
            'Delay in thread 0 completed',
            'Delay in thread 1 completed',
            'Delay in thread 2 completed',
        ]
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_custom_number_of_threads(self):
        output = task_func(0.1, 5)
        expected_output = [
            'Delay in thread 0 completed',
            'Delay in thread 1 completed',
            'Delay in thread 2 completed',
            'Delay in thread 3 completed',
            'Delay in thread 4 completed',
        ]
        self.assertEqual(sorted(output), sorted(expected_output))
        
    def test_zero_threads(self):
        output = task_func(1, 0)
        self.assertEqual(output, [])  # No threads to complete

    def test_negative_delay_time(self):
        with self.assertRaises(ValueError):  # Example expectation. Change as per actual implementation behavior if needed.
            task_func(-1, 5)

if __name__ == '__main__':
    unittest.main()