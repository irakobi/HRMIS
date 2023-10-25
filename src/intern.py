"""
AndrewId: ymfitumu
"""

# importing module 'Employee'
from employee import Employee


class Intern(Employee):
    """
    A subclass that stores Intern's details and earnings.

    parameters:
        university_name (str): university name of the intern
        program_name(str): program name of the intern
        internship_duration(float): internship duration of the intern

    methods:
        __init__, get_university_name, get_program_name,
         get_internship_duration, set_internship_duration,
         calculate_earnings, __str__
    """

    def __init__(self, employee_id: str, first_name: str, last_name: str,
                 email: str, telephone_number: str, bank_account_number: str,
                 salary: float, university_name: str, program_name: str,
                 internship_duration: float):
        """
        Initializes intern class attributes.

        parameters:
            university_name (str): university name of the intern
            program_name(str): program name of the intern
            internship_duration(float): internship duration of the intern

        returns: none
        """
        # Inheriting attributes from the parent class
        super().__init__(employee_id, first_name, last_name, email,
                         telephone_number, bank_account_number, salary)
        # Initialize additional instances as private with the provided inputs
        self.__university_name = university_name
        self.__program_name = program_name
        self.__internship_duration = internship_duration

    def get_university_name(self):
        """
        Gets the university name of the intern.

        parameters: none

        returns:
            str: the university name of the intern.
        """
        return self.__university_name

    def get_program_name(self):
        """
        Gets the program name of the intern.

        parameters: none

        returns:
            str: the program name of the intern.
        """
        return self.__program_name

    def get_internship_duration(self):
        """
        Gets the internship duration of the intern.

        parameters: none

        returns:
            str: the internship duration of the intern.
        """
        return self.__internship_duration

    def set_internship_duration(self, new_internship_duration):
        """
        Sets the internship duration of the intern.

        parameters:
            new_internship_duration (float)

        returns: none
        """
        self.__internship_duration = new_internship_duration

    def calculate_earnings(self):
        """
        Calculates and returns earnings of the intern.

        parameters: none

        returns:
            float: total earnings of the intern.
        """
        # Compute director's total earnings
        total_earnings = self.get_salary() * (self.__internship_duration/12)

        return total_earnings

    def __str__(self):
        """
        Displays information of the intern.

        parameters: none

        returns:
            str: Information of the intern.
        """
        return (f'{super().__str__()}\n'
                f'University: {self.__university_name}\n'
                f'Program: {self.__program_name}\n'
                f'Internship duration: {self.__internship_duration}')


