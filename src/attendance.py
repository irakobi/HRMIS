
from datetime import datetime
import json

class Attendance:
    """This class Represents attendance records for each employee, including
        date, in-time, and out-time, it will record and display the attendance.
        Again it calculate the working hours.

        Attributes:
                o date: The current date of the attendance.
                o in_time: The time employee enters or arrive to the job
                o out_time: The time employee leave the job
                o employee_id: the empolyee ID 
    """

    # Dictionary to store attendance records
    attendance_records = {}

    def __init__(self, employee_id: str, department: str, 
                date: str, in_time: str, out_time: str) -> None:
        
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        self.employee_id = employee_id
        self.department = department
        

    def record_attendance(self) -> dict:
        """This function record attendance attributes a dictionary.

           parameter:
                    date: String
                    in_time: String
                    out_time: String
                    employee_id: String
                    department: String
           return:dict
        """
        # dictionary with the key
        attendance_dict = {}
        attendance_dict['Employee ID'] = self.employee_id
        attendance_dict['Department'] = self.department
        attendance_dict['Date'] = self.date
        attendance_dict['In time'] = self.in_time
        attendance_dict['Out time'] = self.out_time

        return attendance_dict
    
    def display_employee_attendance(employee_id):
        """ Display attendance records for individual employees.
            Args:
                employee_id (str): The ID of the employee whose attendance records you want to display.
            Returns:
                str: A representation of the attendance records.
        """
        try:
             # Load the JSON file into the attendance_records list of dictionaries
            with open('attendance record.json', 'r') as file:
             attendance_records = json.load(file)

            # Initialize a flag to check if the employee_id is found
            employee_found = False

            # Iterate through the attendance_records list of dictionaries
            print(f'------The attendance record for the employee with ID: {employee_id} ------\n')
            for record in attendance_records:
                if record['Employee ID'] == employee_id:
                    # Employee found, print their attendance records
                    employee_found = True
                    print(f"Employee ID: {record['Employee ID']},\
                    \nDepartment: {record['Department']},\
                    \nDate: {record['Date']},\
                    \nIn time: {record['In time']},\
                    \nOut time: {record['Out time']}\n")
                   
            if not employee_found:
                print(f"Employee with ID {employee_id} not found in attendance records.")

        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
    def display_team_attendance(department):
        """ Display attendance records for whole team or department of employees.
            return:
                String: the representation of attendance record.
        """
        try:
        # Load the JSON file into the attendance_records dictionary
            with open('attendance record.json', 'r') as file:
                attendance_records = json.load(file)


            # Initialize a flag to check if the department is found
            department_found = False

            # Iterate through the attendance_records list of dictionaries
            print(f'------The attendance record for the employee with ID: {department} ------\n')
            print(f'The department: {department}\n')
            for record in attendance_records:
                if record['Department'] == department:
                    # department found, 
                    department_found = True
                    print(f"Employee ID: {record['Employee ID']},\
                    \nDate: {record['Date']},\
                    \nIn time: {record['In time']},\
                    \nOut time: {record['Out time']}\n")

            if not department_found:
                print(f"The team of {department} not found in attendance records.")
                

        except FileNotFoundError:
            print("Error: File not found.")
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_attendance_summary():
        """ Display attendance summary for the all employees.
            return:
                String: the representation of attendance records.
        """
        try:
            # Load the JSON file into the attendance_records list of dictionaries
            with open('attendance record.json', 'r') as file:
                attendance_records = json.load(file)

            # Sort attendance records by department and date
            sorted_records = sorted(attendance_records, key=lambda x: (x['Department'], x['Date']))

            current_department = None
            for record in sorted_records:
                if record['Department'] != current_department:
                    print(f'\n------The attendance summary for {record["Department"]} department------\n')
                    current_department = record['Department']

                print(f"Employee ID: {record['Employee ID']}, Date: {record['Date']}, In time: {record['In time']}, Out time: {record['Out time']}")

        except FileNotFoundError:
            print("Error: File not found.")
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def calculate_worked_hours(self, attendance) -> float:
        """This function calculate the daily worked hours.

           parameter:
                    in_time: String
                    out_time: String
           return: float   
        """
        # Converting string into real date
        in_time_converted = datetime.strptime(attendance['In time'], "%H:%M")
        out_time_converted = datetime.strptime(attendance['Out time'], "%H:%M")
        working_time = out_time_converted - in_time_converted  # in seconds
        # Convert seconds to hours
        working_hours = working_time.total_seconds() / 3600

        return working_hours
    
    

#The main function to execute the whole program
if __name__ == "__main__":
    attendance = Attendance('1234', 'EPE', '12-11-2022', '12:30', '16:30')
    attendance_dict = attendance.record_attendance()

    attendance_list = [attendance_dict]

    print(attendance.calculate_worked_hours(attendance_dict))
    # Attendance.display_team_attendance('ECE')
    Attendance.display_attendance_summary()

    def load_objects_from_json(filename):
        """
        Load objects from a JSON file.

        Args:
            filename (str): The name of the JSON file to read objects from.
        Returns:
            list: A list of objects read from the JSON file.
        """
        try:
            with open(filename, 'r') as json_file:
                objects = json.load(json_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
        # If the file doesn't exist, return an empty list
            objects = []
        return objects

    def dump_to_json_file(filename, data):
        """
        Save a list of objects to a JSON file.

        Args:
            filename (str): The name of the JSON file to save the objects to.
            data (list): A list of objects to be saved to the JSON file.
        """
        # read the existing list of attendances

        current_list = load_objects_from_json('attendance record.json')
        combined = current_list + data
        
        try:
            with open(filename, 'w') as file:
                json.dump(combined, file, indent=4)
            print(f"Data has been successfully appended to {filename}")
        except Exception as e:
            print(f"An error occurred while appending to {filename}: {str(e)}")

    # dump_to_json_file('attendance record.json', attendance_list)


    

