import pandas as pd
import unittest
from datetime import datetime

# Here is your prompt:
def task_func(data, date_format, country, country_codes=None):
    """ 
    Draw a histogram of the data from a DataFrame column of the pandas after converting the data into a specific format,
    and return the matplotlib Axes object.

    Parameters:
    data (DataFrame): The pandas DataFrame containing date strings. The DataFrame has a column named 'dates' with the format '%d/%m/%Y'
    date_format (str): The date format string.
    country (str): The country name.
    country_codes (dict, optional): A dictionary mapping country names. Defaults to a predefined dictionary, where default is:
        default_country_codes = {
            'Russia': 'ru_RU',
            'Germany': 'de_DE',
            'France': 'fr_FR',
            'Spain': 'es_ES',
            'Italy': 'it_IT'
        }

    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted histogram.

    Raises:
    ValueError: If 'data' is not a DataFrame, 'date_format' is not a string, 'country' is not in 'country_codes',
                or 'country_codes' is not a dictionary.

    Additional Notes:
    The title of the plot should be 'Date Distribution'. The y label should be named with 'Frequency'.
    
    Requirements:
    - pandas
    - datetime

    Example:
    >>> data = pd.DataFrame({'dates': ['01/01/2000', '01/02/2000', '02/03/2000', '04/05/2000', '06/07/2000']})
    >>> ax = task_func(data, '%d/%m/%Y', 'Russia')
    >>> ax.get_title()
    'Date Distribution'
    """

               default_country_codes = {
        'Russia': 'ru_RU',
        'Germany': 'de_DE',
        'France': 'fr_FR',
        'Spain': 'es_ES',
        'Italy': 'it_IT'
    }

    if country_codes is None:
        country_codes = default_country_codes

    if not isinstance(data, pd.DataFrame) or not isinstance(date_format, str) or not isinstance(country_codes, dict):
        raise ValueError("Invalid input types.")
    if country not in country_codes:
        raise ValueError(f"Country '{country}' not found in country codes.")

    try:
        data['parsed_dates'] = data['dates'].apply(lambda x: datetime.strptime(x, date_format).date())
    except ValueError:
        raise ValueError("Date format mismatch.")

    ax = data['parsed_dates'].hist()
    ax.set(title='Date Distribution', ylabel='Frequency')
    return ax


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_input(self):
        data = pd.DataFrame({'dates': ['01/01/2000', '01/02/2000', '02/03/2000']})
        ax = task_func(data, '%d/%m/%Y', 'Russia')
        self.assertEqual(ax.get_title(), 'Date Distribution')
    
    def test_invalid_data_type(self):
        with self.assertRaises(ValueError) as context:
            task_func("invalid_data", '%d/%m/%Y', 'Russia')
        self.assertEqual(str(context.exception), "Invalid input types.")
    
    def test_invalid_date_format_type(self):
        data = pd.DataFrame({'dates': ['01/01/2000']})
        with self.assertRaises(ValueError) as context:
            task_func(data, 12345, 'Russia')  # Invalid date format type
        self.assertEqual(str(context.exception), "Invalid input types.")

    def test_country_not_in_country_codes(self):
        data = pd.DataFrame({'dates': ['01/01/2000']})
        with self.assertRaises(ValueError) as context:
            task_func(data, '%d/%m/%Y', 'UnknownCountry')  # Invalid country
        self.assertEqual(str(context.exception), "Country 'UnknownCountry' not found in country codes.")
    
    def test_date_format_mismatch(self):
        data = pd.DataFrame({'dates': ['01-01-2000', '01-02-2000']})  # Incorrect date format
        with self.assertRaises(ValueError) as context:
            task_func(data, '%d/%m/%Y', 'Russia')
        self.assertEqual(str(context.exception), "Date format mismatch.")


if __name__ == '__main__':
    unittest.main()