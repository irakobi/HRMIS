import unittest
from io import StringIO
from unittest.mock import patch
from salary import Salary
from employee import Employee
from manager import Manager
from director import Director
from intern import Intern

class TestSalary(unittest.TestCase):
    """
    This class test the main functions in the salary class.
    methods:
            o test_calculate_monthly_salary(self)
            o test_display_monthly_salary(self)

    """
    
    def test_calculate_monthly_salary(self):
        """Function to test the calculate_monthly_salary().
        """
        salary = Salary(0.2)
        employee = Employee('1234', 'Obed', 'Irakoze', 'obed@cmu.com', '0788888888', 60000)
        monthly_salary = salary.calculate_monthly_salary(employee)
        # for the tax of 20%
        self.assertEqual(monthly_salary, 4000)  

    def test_display_monthly_salary(self):
        """
        Function to test display_monthly_salary().
        """
        salary = Salary(0.2)
        employee1 = Employee('1234', 'Obed', 'Irakoze', 'obed@cmu.com', '0788888888', 60000)
        employee2 = Employee('4321', 'Yves', 'Ndayisaba', 'yves@cmu.com', '0799999999', 75000)
        employee_objects = [employee1, employee2]

        # Redirect standard output to capture printed data
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            salary.display_monthly_salary(employee_objects)

        # Reset standard output
        captured_output.seek(0)
        output = captured_output.read()

        # Check for key elements in the output
        self.assertIn("Employee name", output)
        self.assertIn("Base salary", output)
        self.assertIn("Net pay", output)
        self.assertIn("Obed Irakoze", output)  
        self.assertIn("Yves Ndayisaba", output) 

if __name__ == '__main__':
    unittest.main()