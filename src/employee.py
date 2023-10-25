class Employee:
    """
    The Base class that has basic attribute of the employee,
    and implement the method of calculate_earnings().

    Attributes:
        o employee_id: A unique identifier for the employee.
        o first_name: First name of the employee.
        o last_name: Last name of the employee.
        o email: Email address of the employee.
        o salary: the annual salary of the employee in dollars.
        o loan_on_salary: The annual loan on salary of the employee in dollars.

    """
    #The constructor that initializes the all attributes.
    def __init__(
            self,
            employee_id: str,
            first_name: str,
            last_name: str,
            email: str,
            salary: float,
            loan_on_salary: float) -> None:
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__salary = salary
        self.__loan_on_salary = loan_on_salary

    #The getter for employee ID
    def get_employee_id(self) -> None:
        """The function that return the employee_id.
           return:
                float:employee_id(A unique identifier for the employee.)
        """
        return self.__employee_id
    
    #The getter for firstname
    def get_first_name(self) -> None:
        """The function that return the first name.
           return:
                String:__first_name(first name of the employee.)
        """
        return self.__first_name
    
    #The getter for firstname
    def get_last_name(self) -> None:
        """The function that return the last name.
           return:
                String:__last_name(last name of the employee.)
        """
        return self.__last_name
    
    #The getter for salary
    def get_salary(self) -> None:
        """The function that return the salary.
           return:
                float:__salary(The annual salary of the employee in dollars.)
        """
        return self.__salary
    
    #The getter for loan on salary
    def get_loan_on_salary(self) -> None:
        """The function that return the loan on salary.
           return:
                float:__loan_on_salary(The annual loan on salary of the employee in dollars.)
        """
        return self.__loan_on_salary
    
    #The getter for email
    def get_email(self) -> None:
        """The function that return the email.
           return:
                float:__email(Email address of the employee.)
        """
        return self.__email
    
     #The the setter for salary
    def set_salary(self, salary) -> None:
        """The function that set the new Salary."""
        self.__salary = salary
    
     #The the setter for loan on salary
    def set_loan_on_salary(self, loan_on_salary) -> None:
        """The function that set the new loan_on_salary."""
        self.__loan_on_salary = loan_on_salary


    #The function to calculate the employee earnings
    def calculate_earnings(self) -> float:
        """The function that calculate the earnings.
           Args:
                float:The rate or bonus for calculating earnings on the salary.  
                float: salary(The salary of employee)
           return:
                float:The earnings based on rate or bonus.
        """
        return 0
    
    def calculate_allowable_loan(self):
        # The method to valculate the allowable loan limit in calculate_allowable_loan method
        raise NotImplementedError("This method should be implement in calculate_allowable_loan")
    
    # The function to calculate and issue the loan on salary.
    def requesting_loan_on_salary(self, amount) -> float:
        """The function that calculate the allowed loan for the employee and issue the loan on salary.

            Args:
                float:The rate for allowable loan on the salary.
                float: salary(The salary of employee)
            Return:
                float: The loan on salary      
        """
        #Checking if the amount is is allowable ti ussue the loan
        allowable_loan = self.calculate_allowable_loan() 
        if amount <= allowable_loan:
            loan = amount
            self.set_loan_on_salary(self.get_loan_on_salary() + loan)
        else:
            raise ValueError(f"The requested loan amount exceed the loan limit of {allowable_loan}$")

        return loan
    
    #The function to display the basic employee information
    def __str__(self) -> str:
       """The function that display basic employee information.
           Args:
                Class attributes
           return:
                String: The well displayed employee information.
        """ 
       return f'The first name: {self.__first_name}\
                \nThe last name: {self.__last_name}\
                \nThe employee ID: {self.__employee_id}\
                \nThe email: {self.__email}\
                \nThe salary: {self.__salary}$\
                \nThe loan on salary: {self.__loan_on_salary}$'
