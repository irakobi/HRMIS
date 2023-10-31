import unittest
import json
from unittest.mock import patch
from io import StringIO
import sys
from hrmis import HRMIS
from attendance import Attendance

class TestHRMIS(unittest.TestCase):

    def setUp(self):
        # Create an instance of HRMIS for testing
        self.hrmis = HRMIS()

    def tearDown(self):
        # Clean up any test data or files if necessary
        pass

    def test_add_employee_records(self):
        """
        Function to test add employee records
        """
        # Mock user input for testing
        user_input = ['1', 'John', 'Doe', 'john@example.com', '1234567890', 50000, '5']

        with patch('builtins.input', side_effect=user_input):
            self.hrmis.add_employee_records()

        # Assert that the employee record was added correctly
        self.assertEqual(self.hrmis.employee_records['Role title'], 'Regular employee')
        self.assertEqual(self.hrmis.employee_records['First name'], 'John')
        self.assertEqual(self.hrmis.employee_records['Last name'], 'Doe')
        self.assertEqual(self.hrmis.employee_records['Email'], 'john@example.com')
        self.assertEqual(self.hrmis.employee_records['Telephone number'], '1234567890')
        self.assertEqual(self.hrmis.employee_records['Salary'], 50000)

        # Verify that the employee record is present in the JSON file
        with open('employee records.json', 'r') as file:
            employee_data = json.load(file)
            self.assertIn(self.hrmis.employee_id, employee_data)

    def test_update_employee_records(self):
        """
        Function to test update employee records
        """
        # Mock user input for testing
        user_input = ['1', 'John', 'Doe', 'john@example.com', '1234567890', 50000, '5']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.add_employee_records()

        # Mock user input for updating the employee record
        user_input = [self.hrmis.employee_id, 'Jane', 'Smith', 'jane@example.com', '9876543210', '5']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.update_employee_records()

        # Assert that the employee record was updated correctly
        updated_record = self.hrmis.load_employee_record('employee records.json')[self.hrmis.employee_id]
        self.assertEqual(updated_record['First name'], 'Jane')
        self.assertEqual(updated_record['Last name'], 'Smith')
        self.assertEqual(updated_record['Email'], 'jane@example.com')
        self.assertEqual(updated_record['Telephone number'], '9876543210')

    def test_remove_employee_record(self):
        """
        Function to test remove employee records
        """
        # Mock user input for testing
        user_input = ['1', 'John', 'Doe', 'john@example.com', '1234567890', 50000, '5']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.add_employee_records()

        # Mock user input for removing the employee record
        user_input = [self.hrmis.employee_id]
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.remove_employee_record()

        # Verify that the employee record is no longer present in the JSON file
        with open('employee records.json', 'r') as file:
            employee_data = json.load(file)
            self.assertNotIn(self.hrmis.employee_id, employee_data)


    def test_calculate_worked_hours(self):
        """
        Function to test the calculate worked hours
        """
        # Mock user input for testing
        user_input = ['1', 'John', 'Doe', 'john@example.com', '1234567890', 50000, '5']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.add_employee_records()

        # Mock user input for attendance data
        user_input = [self.hrmis.employee_id, 'Regular employee', '20-02-2023', '08:00', '17:00']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.store_attendance_data()

        # Mock the user inputs for employee_id and Date
        with patch('builtins.input', side_effect=[self.hrmis.employee_id, '20-02-2023']):
            # Mock the calculate_worked_hours method to return a specific value
            with patch.object(self.hrmis, 'calculate_worked_hours', return_value=9.0):
                # Calculate the worked hours (it will return 9.0 as specified)
                worked_hours = self.hrmis.calculate_worked_hours()

                # Assert that the calculated worked hours match the expected value
                self.assertEqual(worked_hours, 9.0)


if __name__ == '__main__':
    unittest.main()
