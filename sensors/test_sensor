import unittest
from unittest.mock import patch
from sensor import read_sensor_data  # Replace 'your_module' with the actual module name

class TestSensorData(unittest.TestCase):
    @patch('random.uniform')
    @patch('time.time')
    def test_read_sensor_data(self, mock_time, mock_uniform):
        # Mock the return values
        mock_uniform.side_effect = [25.0, 45.0]  # Mock temperature and humidity
        mock_time.return_value = 1234567890.0  # Mock timestamp

        # Call the function
        result = read_sensor_data()

        # Assertions
        self.assertEqual(result['temperature'], 25.0)
        self.assertEqual(result['humidity'], 45.0)
        self.assertEqual(result['timestamp'], 1234567890.0)

    def test_read_sensor_data_range(self):
        # This test checks if the function returns values within the expected range
        result = read_sensor_data()
        self.assertGreaterEqual(result['temperature'], 20.0)
        self.assertLessEqual(result['temperature'], 30.0)
        self.assertGreaterEqual(result['humidity'], 30.0)
        self.assertLessEqual(result['humidity'], 60.0)

if __name__ == '__main__':
    unittest.main()
