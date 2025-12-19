import unittest
import numpy as np
import matplotlib.pyplot as plt

# Provided prompt
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def task_func(city_dict, max_range=1000000, seed=0):
    if max_range < 1:
        raise ValueError("max_range must be a positive integer")

    np.random.seed(seed)
    city_population = {
        city: (np.random.randint(1, max_range) if city in CITIES else -1) 
        for _, city in city_dict.items() if isinstance(city, str)
    }

    plt.figure()
    ax = plt.bar(city_population.keys(), city_population.values())
    plt.xlabel('City')
    plt.ylabel('Population')
    plt.title('City Populations')

    return city_population, plt.gca()

class TestTaskFunc(unittest.TestCase):

    def test_population_values(self):
        city_dict = {'John': 'New York', 'Alice': 'London'}
        population_dict, _ = task_func(city_dict)
        self.assertIn('New York', population_dict)
        self.assertIn('London', population_dict)
        self.assertGreater(population_dict['New York'], 0)
        self.assertGreater(population_dict['London'], 0)

    def test_city_not_in_list(self):
        city_dict = {'John': 'Fake City'}
        population_dict, _ = task_func(city_dict)
        self.assertEqual(population_dict['Fake City'], -1)

    def test_max_range_parameter(self):
        city_dict = {'John': 'New York'}
        with self.assertRaises(ValueError):
            task_func(city_dict, max_range=0)

    def test_seed_reproducibility(self):
        city_dict = {'John': 'New York', 'Alice': 'London'}
        np.random.seed(0)
        first_call, _ = task_func(city_dict)
        
        np.random.seed(0)
        second_call, _ = task_func(city_dict)
        
        self.assertEqual(first_call, second_call)

    def test_multiple_cities(self):
        city_dict = {
            'John': 'New York', 
            'Alice': 'London', 
            'Bob': 'Beijing', 
            'Charlie': 'Tokyo', 
            'David': 'Unknown City'
        }
        population_dict, _ = task_func(city_dict)
        self.assertEqual(len(population_dict), 4)  # One city should be -1


if __name__ == '__main__':
    unittest.main()