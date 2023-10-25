"""
This module manages salary information.
"""


class Salary:
    """
    This class manages salary information for each employee, including the base
    salary, taxes, bonuses and allowances.
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
        Gets tax rates for the employee salary.

        return:
            float: tax_rate
        """
        return self.tax_rate

    def calculate_monthly_salary(self, employee_object):
        """
        Calculates the monthly salary of each employee

        :return:
        """
        # compute monthly salary of the employee
        monthly_salary = (employee_object.calculate_earnings() -
                          (employee_object.calculate_earnings() *
                           self.tax_rate)) / 12

        return monthly_salary

    def display_salary(self, employee_object):
        """
        Displays the monthly salary of each employee.

        return:
            string: salary of each employee
        """
        # Check the type of employee
        if employee_object.__class__.__name__ == 'Employee':
            print(f"Regular employee salary information"
                  f'-----------------------------------\n'
                  f'Base salary: {employee_object.get_salary()/12}\n'
                  f'Net pay: {(employee_object.calculate_earnings()/12) * self.tax_rate}')
        elif employee_object.__class__.__name__ == 'Manager':
            overtime_amount = (employee_object.get_overtime_pay_per_hour() *
                               employee_object.get_overtime_hours())
            allowance_amount = employee_object.get_salary() * (employee_object.get_allowance_rate() / 100)
            print(f"Manager salary information"
                  f'--------------------------\n'
                  f'Base salary: {employee_object.get_salary()/12}\n'
                  f'Allowance amount: {allowance_amount/12}\n'
                  f'Overtime amount: {overtime_amount/12}\n'
                  f'Net pay: {(employee_object.calculate_earnings()/12) * self.tax_rate}')
        elif employee_object.__class__.__name__ == 'Director':
            overtime_amount = (employee_object.get_overtime_pay_per_hour() *
                               employee_object.get_overtime_hours())
            print(f"Director salary information"
                  f'---------------------------\n'
                  f'Base salary: {employee_object.get_salary()/12}\n'
                  f'Bonus: {employee_object.get_annual_bonus()/12}\n'
                  f'Overtime amount: {overtime_amount/12}\n'
                  f'Net pay: {(employee_object.calculate_earnings()/12) * self.tax_rate}')
        elif employee_object.__class__.__name__ == 'Intern':
            print(f"Intern salary information"
                  f'-------------------------\n'
                  f'Base salary: {employee_object.get_salary()/12}\n'
                  f'Net pay: {(employee_object.calculate_earnings()/12) * self.tax_rate}')
