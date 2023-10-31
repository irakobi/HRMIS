

# importing module 'Employee'
from employee import Employee


class Director(Employee):
    """
    A subclass that stores Director's details and earnings.

    parameters:
        department_name (str): Department of the director
        annual_bonus (float): Annual bonus of the director
        overtime_hours (float): overtime hours worked by the director
        overtime_pay_per_hour (float): overtime amount per hour to be paid to the director

    methods:
        __init__, get_department_name, set_department_name,
        get_annual_bonus, set_annual_bonus, get_overtime_hours,
        set_overtime_hours, get_overtime_pay_per_hour,
        set_overtime_pay_per_hour, calculate_earnings, __str__
    """
    def __init__(self, employee_id: str, first_name: str, last_name: str,
                 email: str, telephone_number: str, salary: float,
                 department_name: str, annual_bonus: float,
                 overtime_hours: float, overtime_pay_per_hour: float):
        """
        Initializes Director class attributes.

        parameters:
        department_name (str): Department of the director
        annual_bonus (float): Annual bonus of the director
        overtime_hours (float): overtime hours worked by the director
        overtime_pay_per_hour (float): overtime amount per hour to be paid to the director


        returns: none
        """
        # Inheriting attributes from the parent class
        super().__init__(employee_id, first_name, last_name, email, telephone_number, salary)
        # Initialize additional instances as private with the provided inputs
        self.__department_name = department_name
        self.__annual_bonus = annual_bonus
        self.__overtime_hours = overtime_hours
        self.__overtime_pay_per_hour = overtime_pay_per_hour

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

    def get_overtime_pay_per_hour(self):
        """
        Gets overtime pay per hour for the director.

        parameters: none

        returns:
            str: overtime amount per hour paid for the director
        """
        return self.__overtime_pay_per_hour

    def set_overtime_pay_per_hour(self, overtime_pay_per_hour):
        """
        Sets overtime pay per hour for the director.

        parameters:
            overtime_pay_per_hour (float): overtime amount per hour
            to be paid to the director

        returns: none
        """
        self.__overtime_pay_per_hour = overtime_pay_per_hour

    def get_overtime_hours(self):
        """
        Gets overtime hours worked by the director.

        parameters: none

        returns:
            float: overtime hours worked by the director
        """
        return self.__overtime_hours

    def set_overtime_hours(self, overtime_hours):
        """
        Sets overtime hours worked by the director.

        parameters:
            overtime_hours (float): overtime hours worked by the director

        returns: none
        """
        self.__overtime_hours = overtime_hours

    def overtime(self):
        """
        Calculates overtime amount of the director.

        return:
            float: overtime amount of the director
        """
        overtime_amount = self.get_overtime_pay_per_hour() * self.get_overtime_hours()

        return overtime_amount

    def calculate_earnings(self):
        """
        Calculates and returns earnings of the director.

        parameters: none

        returns:
            float: total earnings of the director.
        """
        # Compute overtime amount
        overtime_amount = self.get_overtime_pay_per_hour() * self.get_overtime_hours()
        # Compute director's total earnings
        total_earnings = self.get_salary() + self.__annual_bonus + overtime_amount

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
                f'Annual bonus: {self.__annual_bonus}\n'
                f'Overtime hours: {self.__overtime_hours} hours\n'
                f'Overtime pay per hour: ${self.__overtime_pay_per_hour}')


