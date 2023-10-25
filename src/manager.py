from employee import Employee

class Manager(Employee):
    """
    The derived class that has basic attribute from the employee
    and managers attributes,
    and override the method calculate_earnings().

    Attributes:
        o employee_id: A unique identifier for the manager.
        o first_name: First name of the manager.
        o last_name: Last name of the manager.
        o email: Email address of the manager.
        o salary: the annual salary of the manager in dollars.
        o department: The department of manager
        o number_direct_reports: the number of direct report of manager
        o loan_on_salary: The annual loan on salary of the manager in dollars.

    """
    #The constructor that initializes the all attributes.
    def __init__(
            self,
            employee_id: str,
            first_name: str,
            last_name: str,
            email: str,
            salary: float,
            loan_on_salary: float,
            department: str,
            number_direct_reports: int) -> None:
        
        self.department = department
        self.number_direct_reports = number_direct_reports

        #Including the attributes from the base class.
        super().__init__(employee_id, first_name, last_name, email, salary, loan_on_salary)
      

    #Overloading The function to calculate the manager earnings
    def calculate_earnings(self, rate) -> float:
        """The function that calculate the earnings.
           Args:
                float: The rate on the salary(0% to 60%).
                float: salary(The salary of manager)
           return:
                float:The earnings based on rate.
        """
        #Checking if the rate ranges from 0% to 60% unless raise the error.
        if rate >= 0 and rate <= 0.6:
            earning = self.get_salary() + (self.get_salary()*rate)
            return earning
        else:
            raise ValueError("The rate should range from 0% to 60%")
        
    # The function to calculate loan on salary.
    def calculate_allowable_loan(self):
        """The function to calculate allowable loan.
            Args:
               float:salary in dollar
            Return:
               float: allowable loan in dollar   
        """
        return self.get_salary() * 0.6
        
    
    #The function to display the manager information
    def __str__(self) -> str:
       """The function that display manager information.
           Args:
                Class attributes
           return:
                String: The well displayed manager information.
        """ 
       return f'The Manager information\
                \n\n{super().__str__()}\
                \nThe department: {self.department}\
                \nThe number of direct reports: {self.number_direct_reports}'
