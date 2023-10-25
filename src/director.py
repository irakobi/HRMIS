from employee import Employee

class Director(Employee):
    """
    The derived class that has basic attribute from the employee
    and director attributes,
    and override the method calculate_earnings().

    Attributes:
        o employee_id: A unique identifier for the director.
        o first_name: First name of the director.
        o last_name: Last name of the director.
        o email: Email address of the director.
        o salary: the annual salary of the director in dollars.
        o department: The department of director.
        o annual_bonus: The annual bonus.
        o loan_on_salary: The annual loan on salary of the director in dollars.

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
            annual_bonus: float) -> None:
        
        self.department = department
        self.annual_bonus = annual_bonus
        #Including the attributes from the base class.
        super().__init__(employee_id, first_name, last_name, email, salary, loan_on_salary)
        self.meeting_schedule = {}  # Initialize an empty dictionary to store meeting dates and topic.
      

    #Overrding The function to calculate the manager earnings
    def calculate_earnings(self) -> float:
        """The function that calculate the earnings.
           Args:
                float: The annual_bonus for calculating earnings on the salary.
                float: salary(The salary of director)
           return:
                float:The earnings based on annual_bonus.
        """
        
        #Checking if the annual_bonus is not negative and then compute earning.
        if self.annual_bonus >= 0:
            earning = self.get_salary() + self.annual_bonus
            return earning
        else:
            raise ValueError("The annual bonus should be positive amount")
        
        
    # The function to calculate loan on salary.
    def calculate_allowable_loan(self)-> float:
        """The function to calculate allowable loan.
            Args:
               float:salary in dollar
            Return:
               float: allowable loan in dollar   
        """
        return self.get_salary() * 0.8
    
   
    def schedule_board_meeting(self, date, topic) -> None:
        """The function to schedule a board meeting.
            Args:
               dictionary:to store meeting dates and topic
            Return:
               None: append the dictionary 
        """
        # Check if the date is already scheduled for a meeting
        if date in self.meeting_schedule:
            print(f"Meeting on {date} already scheduled.\
                  \nTopic: {self.meeting_schedule[date]}")
        else:
            self.meeting_schedule[date] = topic
            print(f"Meeting on {date} scheduled, topic: {topic}")


    def view_meeting_schedule(self) -> None:
        """The function to display a board meeting.
            Args:
               dictionary:where meeting dates and topic are kept
            Return:
               None: display the meetings 
        """
        # View the entire meeting schedule 
        print("\nThe scheduled board meetings")
        print("\n{:<15} {:<15}".format("Date", "Topic"))
        for date, topic in self.meeting_schedule.items():
            print("{:<15} {:<15}".format(date, topic))

    
    #The function to display the director information
    def __str__(self) -> str:
       """The function that display director information.
           Args:
                Class attributes
           return:
                String: The well displayed director information.
        """ 
       return f'The Director information\
                \n\n{super().__str__()}\
                \nThe department: {self.department}\
                \nThe annual bonus: {self.annual_bonus}'
