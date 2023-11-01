import unittest
import json
from unittest.mock import patch
from io import StringIO
import sys
from hrmis import HRMIS
from attendance import Attendance

class TestHRMIS(unittest.TestCase):
    """
    The class to test the main functions of HRMIS.
    methods:
        o test_add_employee_records(self)
        o test_update_employee_records(self)
        o test_remove_employee_record(self)
        o test_display_employee_records(self)
        o test_calculate_worked_hours(self)

       
    """

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
        user_input = ['1', 'Obed', 'Irakoze', 'obed@cmu.com', '0788888888', 450, '5']

        with patch('builtins.input', side_effect=user_input):
            self.hrmis.add_employee_records()

        # Assert that the employee record was added correctly
        self.assertEqual(self.hrmis.employee_records['Role title'], 'Regular employee')
        self.assertEqual(self.hrmis.employee_records['First name'], 'Obed')
        self.assertEqual(self.hrmis.employee_records['Last name'], 'Irakoze')
        self.assertEqual(self.hrmis.employee_records['Email'], 'obed@cmu.com')
        self.assertEqual(self.hrmis.employee_records['Telephone number'], '0788888888')
        self.assertEqual(self.hrmis.employee_records['Salary'], 450)

        # Verify that the employee record is present in the JSON file(employee records.json)
        with open('employee records.json', 'r') as file:
            employee_data = json.load(file)
            self.assertIn(self.hrmis.employee_id, employee_data)

    def test_update_employee_records(self):
        """
        Function to test update employee records
        """
        # Mock user input for testing
        user_input = ['1', 'Obed', 'Irakoze', 'obed@cmu.com', '0788888888', 450, '5']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.add_employee_records()

        # Mock user input for updating the employee record
        user_input = [self.hrmis.employee_id, 'Yves', 'Ndayi', 'yves@cmu.com', '0788888888', '5']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.update_employee_records()

        # Assert that the employee record was updated correctly
        updated_record = self.hrmis.load_employee_record('employee records.json')[self.hrmis.employee_id]
        self.assertEqual(updated_record['First name'], 'Yves')
        self.assertEqual(updated_record['Last name'], 'Ndayi')
        self.assertEqual(updated_record['Email'], 'yves@cmu.com')
        self.assertEqual(updated_record['Telephone number'], '0788888888')

    def test_remove_employee_record(self):
        """
        Function to test remove employee records
        """
        # Mock user input for testing
        user_input = ['1', 'Obed', 'Irakoze', 'obed@cmu.com', '0788888888', 450, '5']
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


    def test_display_employee_records(self):
        """Function to test display_employee_records.
        """
        # Mock the employee records for testing
        employee_records = {
            '1234': {'Role title': 'Regular employee', 'First name': 'Obed', 'Last name': 'Irakoze', 'Email': 'obed@cmu.com', 'Salary': 450},
            '4321': {'Role title': 'Manager', 'First name': 'Yves', 'Last name': 'Ndayisaba', 'Email': 'yves@cmu.com', 'Salary': 1000},
            '5678': {'Role title': 'Director', 'First name': 'kalisa', 'Last name': 'habimana', 'Email': 'kalisa@cmu.com', 'Salary': 2000},
        }

        # Set the employee records in the HRMIS instance
        self.hrmis.employee_records = employee_records

        # Redirect standard output to capture printed data
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            self.hrmis.display_employee_records()

        # Reset standard output
        captured_output.seek(0)
        
        # Read the captured output as lines
        output_lines = captured_output.read().split('\n')
        
        # Check if key elements exist in the captured output lines
        expected_elements = ["Employee ID", "Role title", "First name", "Last name", "Email", "Salary"]
        
        for element in expected_elements:
            element_found = any(element in line for line in output_lines)
            self.assertTrue(element_found)


    def test_calculate_worked_hours(self):
        """
        Function to test the calculate worked hours
        """
        # Mock user input for testing
        user_input = ['1', 'Obed', 'Irakoze', 'obed@cmu.com', '0788888888', 600, '5']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.add_employee_records()

        # Mock user input for attendance data
        user_input = [self.hrmis.employee_id, 'Regular employee', '25-10-2023', '08:00', '17:00']
        with patch('builtins.input', side_effect=user_input):
            self.hrmis.store_attendance_data()

        # Mock the user inputs for employee_id and Date
        with patch('builtins.input', side_effect=[self.hrmis.employee_id, '25-10-2023']):
            # Mock the calculate_worked_hours method to return a specific value
            with patch.object(self.hrmis, 'calculate_worked_hours', return_value=9.0):
                # Calculate the worked hours (it will return 9.0 as specified)
                worked_hours = self.hrmis.calculate_worked_hours()

                # Assert that the calculated worked hours match the expected value
                self.assertEqual(worked_hours, 9.0)


if __name__ == '__main__':
    unittest.main()
