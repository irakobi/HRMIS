from employee import Employee

class Intern(Employee):
    """
    The derived class that has basic attribute from the employee
    and director attributes,
    and override the method calculate_earnings().

    Attributes:
        o employee_id: A unique identifier for the Intern.
        o first_name: First name of the Intern.
        o last_name: Last name of the Intern.
        o email: Email address of the Intern.
        o salary: the annual salary of the Intern in dollars.
        o university_name:The intern's university name
        o program_name:The program intern study
        o internship_duration:The period of internship
        o loan_on_salary: The annual loan on salary of the intern in dollars.

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
            university_name: str,
            program_name: str,
            internship_duration: int) -> None:
        
        self.university_name = university_name
        self.program_name = program_name
        self.internship_duration = internship_duration
        #Including the attributes from the base class.
        super().__init__(employee_id, first_name, last_name, email, salary, loan_on_salary)
      

    #Overrding The function to calculate the intern earnings
    def calculate_earnings(self) -> float:
        """The function that calculate the earnings.
           Args:
                int: The duration of the internship.
                float: salary(The salary of intern)
           return:
                float:The earnings based on internship duration.
        """
        
        #Checking if the internship_duration ranges from 3 to 6 months.
        if self.internship_duration >= 3 and self.internship_duration <= 6:
            earning = self.get_salary() * (self.internship_duration/12)
            return earning
        else:
            raise ValueError("The internship duration should range between 3 to 6")
        
        
    # The function to calculate loan on salary.
    def calculate_allowable_loan(self):
        """The function to calculate allowable loan.
           No intern exceed a half of earning as loan.
            Args:
               float:salary in dollar
            Return:
               float: allowable loan in dollar for internship duration.  
        """
        return (self.get_salary() * 0.5)*(self.internship_duration/12)
        
        
    
    #The function to display the director information
    def __str__(self) -> str:
       """The function that display intern information.
           Args:
                Class attributes
           return:
                String: The well displayed intern information.
        """ 
       return f'The Intern information\
                \n\n{super().__str__()}\
                \nThe University name: {self.university_name}\
                \nThe program name: {self.program_name}\
                \nThe Duration of internship: {self.internship_duration} months'