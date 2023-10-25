
from datetime import datetime

class Attendance:
    """This class Represents attendance records for each employee, including
        date, in-time, and out-time, it will record and display the attendance.
        Again it calculate the working hours.

        Attributes:
                o date: The current date of the attendance.
                o in_time: The time employee enters or arrive to the job
                o out_time: The time employee leave the job
    """

    def __init__(self, employee_id:str, date:str, in_time: str, out_time: str) -> None:
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        self.employee_id = employee_id
        self.attendance_dict = {} 

    def record_attendance(self) ->dict:
        """This function record attendance attributes a dictionary.

           parameter:
                    date: String
                    in_time: String
                    out_time: String
                    employee_id: String
           return:dict
        """
        # dictionary with the key
        self.attendance_dict['Employee ID'] = self.employee_id
        self.attendance_dict['Date'] = self.date
        self.attendance_dict['In time'] = self.in_time
        self.attendance_dict['Out time'] = self.out_time

        return self.attendance_dict
    def calculate_worked_hours(self) ->float:
        """This function calculate the daily worked hours.

           parameter:
                    in_time: String
                    out_time: String
           return: float
        """
        # Converting string into real date
        in_time_coverted= datetime.strptime(self.in_time, "%H:%M")
        out_time_coverted = datetime.strptime(self.out_time, "%H:%M")
        working_time = out_time_coverted - in_time_coverted # in seconds
        # Convert seconds to hours
        working_hours = working_time.total_seconds() / 3600

        return working_hours
    def __str__(self) -> str:
        return f"{self.employee_id} {self.in_time} {self.out_time}" 


