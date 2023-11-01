

class Employee:
    """
    A super class that stores employee details and earnings.

    parameters:
        employee_id (str): A unique identifier for the employee
        first_name (str): First name of the employee
        last_name (str): Last name of the employee
        email (str): Email address of the employee
        telephone_number (str): Telephone number of the employee
        salary (float): The annual salary of the employee in dollars

    methods:
        __init__, get_employee_id, get_name, set_first_name,
        set_last_name, get_email, set_email, get_telephone_number,
        set_telephone_number, get_salary, set_salary,
        calculate_earnings, __str__
    """
    def __init__(self, employee_id: str, first_name: str, last_name: str,
                 email: str, telephone_number: str, salary: float):
        """
        Initializes Employee class attributes.

        parameter:
            employee_id (str): A unique identifier for the employee
            first_name (str): First name of the employee
            last_name (str): Last name of the employee
            email (str): Email address of the employee
            telephone_number (str): Telephone number of the employee
            salary (float): The annual salary of the employee in dollars

        returns: none
        """
        # Initialize instances as private with the provided inputs
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__telephone_number = telephone_number
        self.__salary = salary

    def get_employee_id(self):
        """
        Gets the employee Id.

        parameters: none

        returns:
            str: employee Id
        """
        return self.__employee_id

    def get_name(self):
        """
        Gets the name of the employee.

        parameters: none

        returns:
            str: The name of the employee.
        """
        return f'{self.__first_name} {self.__last_name}'

    def set_first_name(self, new_first_name):
        """
        Sets the name of the employee.

        parameters:
            new_first_name (str): The new first name of the employee.

        returns: none
        """
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        """
        Sets the last name of the employee.

        parameters:
            new_last_name (str): The new last name of the employee.

        returns: none
        """
        self.__last_name = new_last_name

    def get_email(self):
        """
        Gets the email address of the employee.

        parameters: none

        returns:
            str: email of the employee.
        """
        return self.__email

    def set_email(self, new_email):
        """
        Sets the email address of the employee.

        parameters:
            new_email (str): The new email address of the employee

        returns: none
        """
        try:
            # Check if an email in valid
            if '@' not in new_email:
                raise ValueError('Invalid email format')
            else:
                self.__email = new_email  # updating email
        except ValueError as e:
            # Handle the error gracefully
            print(f'Error: {e}')

    def get_telephone_number(self):
        """
        Gets the telephone number of the employee.

        parameters: none

        returns:
            str: telephone number of the employee.
        """
        return self.__telephone_number

    def set_telephone_number(self, new_telephone_number):
        """
        Sets the telephone number of the employee.

        parameters:
            new_telephone_number (str): new telephone number of the employee

        returns: none
        """
        try:
            # Check if telephone number in valid
            if '+' not in new_telephone_number:
                raise ValueError('Telephone number should start with "+"')
            else:
                self.__telephone_number = new_telephone_number  # updating telephone number
        except ValueError as e:
            # Handle the error gracefully
            print(f'Error: {e}')

    def get_salary(self):
        """
        Gets the annual salary of the employee.

        parameters: none

        returns:
            str: email of the employee.
        """
        return self.__salary

    def __set_salary(self, new_salary):
        """
        Sets the annual salary of the employee.

        parameters:
            new_salary (float): The new annual salary of the employee.

        returns: none
        """
        self.__salary = new_salary

    def update_salary(self, amount):
        """
        Updates the annual salary of the employee.

        parameters:
            amount (float): The amount to be added to the salary of the employee.

        returns: none
        """
        try:
            # Check if amount is positive and not zero
            if amount <= 0:
                raise ValueError('Amount must be greater then zero')
            else:
                new_salary = self.get_salary() + amount  # incrementing salary
                self.__set_salary(new_salary)  # updating salary

        except ValueError as e:
            # Handle the error gracefully
            print(f'Error: {e}')

    def calculate_earnings(self):
        """
        Calculates and returns earnings of the employee.

        parameters: none

        returns:
            float: total earnings of the employee.
        """

        # Compute employee's total earnings
        total_earnings = self.__salary

        return total_earnings

    def __str__(self):
        """
        Displays information of the employee.

        parameters: none

        returns:
            str: Information of the employee
        """
        return (f'Employee ID: {self.__employee_id}\n'
                f'First name: {self.__first_name}\n'
                f'Last name: {self.__last_name}\n'
                f'Email: {self.__email}\n'
                f'Telephone number: {self.__telephone_number}\n'
                f'Salary: ${self.__salary}')
