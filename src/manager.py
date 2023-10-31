"""
AndrewId: ymfitumu
"""

# importing modules
from employee import Employee


class Manager(Employee):
    """
    A subclass that stores manager details and earnings.

    parameters:
        department_name (str): Department of the manager
        direct_reports_number (int): Direct reports of the manager
        allowance_rate (float): management support allowance rate of the salary

    methods:
        __init__, get_department_name, set_department_name, get_direct_reports_number,
        set_direct_reports_number, calculate_earnings, __str__
    """
    def __init__(self, employee_id: str, first_name: str, last_name: str, email: str,
                 telephone_number: str, salary: float, department_name: str,
                 direct_reports_number: int, allowance_rate: float):
        """
        Initializes Manager class attributes.

        parameters:
            department_name (str): Department of the manager
            direct_reports_number (int): Direct reports of the manager
            allowance_rate (float): management support allowance rate of the salary
        returns: none
        """
        # Inheriting attributes from the parent class
        super().__init__(employee_id, first_name, last_name, email,
                         telephone_number, salary)
        # Initialize additional instances as private with the provided inputs
        self.__department_name = department_name
        self.__direct_reports_number = direct_reports_number
        self.__allowance_rate = allowance_rate

    def get_department_name(self):
        """
        Gets the department of the manager.

        parameters: none

        returns:
            str: department name of the manager.
        """
        return self.__department_name

    def set_department_name(self, new_department_name):
        """
        Sets the department name of the manager.

        parameters:
            new_department_name (str): New department name of the manager

        returns: none
        """
        self.__department_name = new_department_name

    def get_direct_reports_number(self):
        """
        Gets the direct reports number of the manager.

        parameters: none

        returns:
            str: the direct reports number of the manager.
        """
        return self.__direct_reports_number

    def set_direct_reports_number(self, direct_reports_number):
        """
        Sets the direct reports number of the manager.

        parameters:
            director_reports_number (str): The direct reports number of the manager

        returns: none
        """
        self.__direct_reports_number = direct_reports_number

    def get_allowance_rate(self):
        """
        Gets management support allowance rate for the manager.

        parameters: none

        returns:
            float: management support allowance rate for the manager
        """
        return self.__allowance_rate

    def set_allowance_rate(self, allowance_rate):
        """
        Sets management support allowance rate for the manager.

        parameters:
            allowance_rate (float): management support allowance rate
            for the manager

        returns: none
        """
        try:
            # Check if rate is in range
            if 0 <= allowance_rate <= 60:
                # Update management support allowance amount
                self.__allowance_rate = allowance_rate
            else:
                # display error
                raise ValueError('Rate must range from 0% to 60%')
        except ValueError as e:
            # Handle the error gracefully
            print(f'Error: {e}')

    def calculate_earnings(self):
        """
        Calculates and returns earnings of the manager.

        parameters: none
        returns:
            float: total earnings of the manager.
        """
        # Compute allowance amount
        allowance_amount = self.get_salary() * (self.__allowance_rate/100)
        # compute total earnings of the manager
        total_earnings = self.get_salary() + allowance_amount
        return total_earnings

    def __str__(self):
        """
        Displays information of the manager.

        parameters: none

        returns:
            str: Information of the manager.
        """
        return (f'{super().__str__()}\n'
                f'Department: {self.__department_name}\n'
                f'Direct reports number: {self.__direct_reports_number}\n'
                f'Management support allowance rate: {self.__allowance_rate}%\n')
