

# importing module 'Employee'
from employee import Employee


class Director(Employee):
    """
    A subclass that stores Director's details and earnings.

    parameters:
        department_name (str): Department of the director
        annual_bonus (float): Annual bonus of the director

    methods:
        __init__, get_department_name, set_department_name,
        get_annual_bonus, set_annual_bonus
    """
    def __init__(self, employee_id: str, first_name: str, last_name: str,
                 email: str, telephone_number: str, salary: float,
                 department_name: str, annual_bonus: float):
        """
        Initializes Director class attributes.

        parameters:
        department_name (str): Department of the director
        annual_bonus (float): Annual bonus of the director


        returns: none
        """
        # Inheriting attributes from the parent class
        super().__init__(employee_id, first_name, last_name, email, telephone_number, salary)
        # Initialize additional instances as private with the provided inputs
        self.__department_name = department_name
        self.__annual_bonus = annual_bonus

    def get_department_name(self):
        """
        Gets the department of the director.

        parameters: none

        returns:
            str: department name of the director.
        """
        return self.__department_name

    def set_department_name(self, new_department_name):
        """
        Sets the department name of the director.

        parameters:
            new_department_name (str)

        returns: none
        """
        self.__department_name = new_department_name

    def get_annual_bonus(self):
        """
        Gets the annual bonus of the director.

        parameters: none

        returns:
            str: the annual bonus of the director.
        """
        return self.__annual_bonus

    def set_annual_bonus(self, new_annual_bonus):
        """
        Sets the annual bonus of the director.

        parameters:
            new_annual_bonus (float)

        returns: none
        """
        self.__annual_bonus = new_annual_bonus

    def calculate_earnings(self):
        """
        Calculates and returns earnings of the director.

        parameters: none

        returns:
            float: total earnings of the director.
        """
        # Compute director's total earnings
        total_earnings = self.get_salary() + self.__annual_bonus

        return total_earnings

    def __str__(self):
        """
        Displays information of the director.

        parameters: none

        returns:
            str: Information of the director.
        """
        return (f'{super().__str__()}\n'
                f'Department: {self.__department_name}\n'
                f'Annual bonus: {self.__annual_bonus}\n')


