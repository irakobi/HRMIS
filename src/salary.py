"""
This module manages salary information.
"""

import pandas as pd
from tabulate import tabulate


class Salary:
    """
    This class manages salary information for each employee, including the base
    salary, taxes, bonuses and allowances.

    Methods:
        get_tax_rate, set_tax_rate, calculate_monthly_salary, display_salary.
    """

    def __init__(self, tax_rate: float):
        """
        Initializes the attributes of the class.

        parameter:
            taxes: float

        return: none
        """
        self.tax_rate = tax_rate

    def get_taxes(self):
        """
        Gets tax rate for the employee salary.
        return:
            float: tax_rate
        """
        return self.tax_rate

    def set_taxes(self, new_tax_rate):
        """
        Sets tax rate for the employee salary.
        parameter:
            tax_rate: tax rate for the employee salary
        """
        self.tax_rate = new_tax_rate

    def calculate_monthly_salary(self, employee_object):
        """
        Calculates the monthly salary of each employee
        return: net monthly salary
        """
        # compute monthly salary of the employee
        salary_untaxed = employee_object.calculate_earnings()/12
        tax_amount = salary_untaxed * self.tax_rate
        net_monthly_salary = salary_untaxed - tax_amount

        return net_monthly_salary

    def display_monthly_salary(self, employee_object):
        """
        Display the monthly salary of an employee.

        parameter:
            employee_object: object of the given class.
        """
        # Check the type of employee and generate a payslip
        if employee_object.__class__.__name__ == 'Employee':
            salary_components = [[employee_object.get_name(), employee_object.get_salary()/12,
                                  self.calculate_monthly_salary(employee_object)]]
            headers = ['Employee name', 'Base salary', 'Net pay']
            salary_records = tabulate(salary_components, headers, tablefmt='fancy_grid')  # Create a table
            print(salary_records)  # Display the table

        elif employee_object.__class__.__name__ == 'Manager':
            # Compute allowance amount
            allowance_amount = employee_object.get_salary() * (employee_object.get_allowance_rate() / 100)
            salary_components = [[employee_object.get_name(), employee_object.get_salary() / 12,
                                  allowance_amount / 12, employee_object.overtime() / 12,
                                  self.calculate_monthly_salary(employee_object)]]
            headers = ['Employee name', 'Base salary', 'Allowance amount', 'Overtime amount', 'Net pay']
            salary_records = tabulate(salary_components, headers, tablefmt='fancy_grid')  # Create a table
            print(salary_records)  # Display table

        elif employee_object.__class__.__name__ == 'Director':
            salary_components = [[employee_object.get_name(), employee_object.get_salary() / 12,
                                  employee_object.get_annual_bonus()/12, employee_object.overtime() / 12,
                                  self.calculate_monthly_salary(employee_object)]]
            headers = ['Employee name', 'Base salary', 'Bonus', 'Overtime amount', 'Net pay']
            salary_records = tabulate(salary_components, headers, tablefmt='fancy_grid')  # create a table
            print(salary_records)  # Display the table

        elif employee_object.__class__.__name__ == 'Intern':
            salary_components = [[employee_object.get_name(), employee_object.get_salary() / 12,
                                  self.calculate_monthly_salary(employee_object)]]
            headers = ['Employee name', 'Base salary', 'Net pay']
            salary_records = tabulate(salary_components, headers, tablefmt='fancy_grid')  # Create a table
            print(salary_records)  # Display the table


def generate_pay_slip(self):
    """
    Generate a payslip of each employee and store it in a text file
    :param self:
    :return:
    """
