from geopy.distance import geodesic
import folium
import unittest

def task_func(dic):
    """
    Generates a Folium map with markers for specified locations and calculates the geodesic
    distances between each pair of locations.

    Parameters:
        dic (dict): A dictionary with location names as keys and their latitudes and longitudes
                    as values (e.g., {'Location': {'Lat': latitude, 'Lon': longitude}}).

    Returns:
        tuple: A tuple containing a Folium map object and a dictionary with pairs of location
               names as keys and their distances in kilometers as values.

    Raises:
        ValueError: If the input dictionary is empty.
    """
    if not dic:
        raise ValueError("Input dictionary is empty.")

    locations = [(k, v['Lat'], v['Lon']) for k, v in dic.items()]
    distances = {}

    folium_map = folium.Map(location=[locations[0][1], locations[0][2]], zoom_start=4)

    for i in range(len(locations)):
        folium.Marker([locations[i][1], locations[i][2]], popup=locations[i][0]).add_to(folium_map)

        for j in range(i + 1, len(locations)):
            distance = geodesic((locations[i][1], locations[i][2]), (locations[j][1], locations[j][2])).kilometers
            distances[(locations[i][0], locations[j][0])] = distance

    return folium_map, distances

class TestTaskFunc(unittest.TestCase):

    def test_valid_input_multiple_locations(self):
        result = task_func({
            'Place1': {'Lat': 0, 'Lon': 0},
            'Place2': {'Lat': 0, 'Lon': 1},
            'Place3': {'Lat': 1, 'Lon': 1}
        })
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], folium.folium.Map)
        self.assertIsInstance(result[1], dict)
        self.assertEqual(len(result[1]), 3)  # 3 pairs

    def test_no_locations(self):
        with self.assertRaises(ValueError):
            task_func({})

    def test_single_location(self):
        result = task_func({
            'Place1': {'Lat': 0, 'Lon': 0}
        })
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], folium.folium.Map)
        self.assertEqual(result[1], {})  # No distances

    def test_distance_calculation(self):
        result = task_func({
            'Place1': {'Lat': 0, 'Lon': 0},
            'Place2': {'Lat': 0, 'Lon': 1}
        })
        distances = result[1]
        self.assertIn(('Place1', 'Place2'), distances)
        self.assertAlmostEqual(distances[('Place1', 'Place2')], 111.319, places=2)  # Distance in km

    def test_multiple_pairs_distance(self):
        result = task_func({
            'Place1': {'Lat': 0, 'Lon': 0},
            'Place2': {'Lat': 1, 'Lon': 1},
            'Place3': {'Lat': 0, 'Lon': 2}
        })
        distances = result[1]
        self.assertIn(('Place1', 'Place2'), distances)
        self.assertIn(('Place1', 'Place3'), distances)
        self.assertIn(('Place2', 'Place3'), distances)
        self.assertEqual(len(distances), 3)

if __name__ == '__main__':
    unittest.main()