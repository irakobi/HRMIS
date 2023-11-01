import unittest
import json
from attendance import Attendance  

class TestAttendance(unittest.TestCase):

    def setUp(self):
        # instance of the Attendance class for testing
        self.attendance = Attendance('employee123', 'HR', '2023-10-31', '09:00', '17:00')

    def tearDown(self):
        pass

    def test_record_attendance(self):
        """
        Function to test record attendance
        """
        # Test the record_attendance method
        attendance_dict = self.attendance.record_attendance()

        # Check if the returned value is a dictionary
        self.assertIsInstance(attendance_dict, dict)

        # Check if the dictionary contains expected keys
        self.assertIn('Employee ID', attendance_dict)
        self.assertIn('Department', attendance_dict)
        self.assertIn('Date', attendance_dict)
        self.assertIn('In time', attendance_dict)
        self.assertIn('Out time', attendance_dict)

        # Check if the values in the dictionary match the expected values
        self.assertEqual(attendance_dict['Employee ID'], 'employee123')
        self.assertEqual(attendance_dict['Department'], 'HR')
        self.assertEqual(attendance_dict['Date'], '2023-10-31')
        self.assertEqual(attendance_dict['In time'], '09:00')
        self.assertEqual(attendance_dict['Out time'], '17:00')

    def test_load_attendance_from_json(self):
        """
        Function to test load attendance from json
        """
        # Test the load_attendance_from_json method
        # Create a temporary JSON file with some data for testing
        test_data = [
            {
                'Employee ID': 'employee1',
                'Department': 'HR',
                'Date': '2023-10-31',
                'In time': '09:00',
                'Out time': '17:00',
            },
            {
                'Employee ID': 'employee2',
                'Department': 'IT',
                'Date': '2023-11-01',
                'In time': '10:00',
                'Out time': '18:00',
            }
        ]

        with open('test_attendance.json', 'w') as json_file:
            json.dump(test_data, json_file)

        # Test the method to load data from the temporary JSON file
        loaded_data = self.attendance.load_attendance_from_json('test_attendance.json')

        # Check if the loaded data is a list
        self.assertIsInstance(loaded_data, list)

        # Check if the loaded data matches the expected data
        self.assertEqual(loaded_data, test_data)

    def test_dump_to_json_file(self):
        """
        Function to test dump to json file
        """
        # Test the dump_to_json_file method
        # Create a temporary JSON file with some data for testing
        test_data = [
            {
                'Employee ID': 'employee1',
                'Department': 'HR',
                'Date': '2023-10-31',
                'In time': '09:00',
                'Out time': '17:00',
            },
        ]

        with open('test_attendance.json', 'w') as json_file:
            json.dump(test_data, json_file)

        # Create additional data to be appended
        additional_data = [
            {
                'Employee ID': 'employee2',
                'Department': 'IT',
                'Date': '2023-11-01',
                'In time': '10:00',
                'Out time': '18:00',
            },
        ]

        # Test the method to append data to the temporary JSON file
        self.attendance.dump_to_json_file('test_attendance.json', additional_data)

        # Load the data from the updated file
        with open('test_attendance.json', 'r') as json_file:
            loaded_data = json.load(json_file)

        # Check if the loaded data contains the additional data
        self.assertIn(additional_data[0], loaded_data)

if __name__ == '__main__':
    unittest.main()
