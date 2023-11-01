import json
import random
import string
from datetime import datetime
from prettytable import PrettyTable
from attendance import Attendance
from salary import Salary
from director import Director
from manager import Manager
from intern import Intern
from employee import Employee


class HRMIS(Attendance):
    """
       records, attendance, and salary calculations.
    """ 

    def __init__(self):
        # create a dictionary to store employee records
        self.employee_records = {}
        self.records = [self.employee_records]


    def load_employee_record(self, filename):

        try:
            with open(filename, 'r') as file:
                    database = json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
        # If the file doesn't exist, return an empty dict
            database = {}

        return database

    def write_records_to_json(self, filename):

        employee_record = self.load_employee_record('employee records.json')
        employee_record[self.employee_id] = self.employee_records

        try:
            with open(filename, 'w') as file:
                json.dump(employee_record, file, indent=4)
            print('Employee records added successfully')

        except FileNotFoundError:
            print('File not found')

    def update_records_to_json(self, updated_record, filename):


        try:
            with open(filename, 'w') as file:
                json.dump(updated_record, file, indent=4)
            print('Employee records file updated successfully')

        except FileNotFoundError:
            print('File not found')

    def generate_employee_id(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(8))
    

    def add_employee_records(self):
        """
        Adds records of the employee
        return: none
        """    
        while True:
            print('Choose the employee role\n\n'
              '1. Regular employee\n'
              '2. Manager\n'
              '3. Director\n'
              '4. Intern\n'
              '5. Back\n')
            option = input('Enter your choice: ')
            # Check for the option and perform required task
            if option == '1':

                print('Fill in the following:')
                self.employee_id = self.generate_employee_id()
                self.employee_records['Role title'] = 'Regular employee'
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = float(input('Salary: '))

                # Store employee records in a json file
                self.write_records_to_json('employee records.json')

            elif option == '2':
                print('Fill in the following:')
                employee_id = self.generate_employee_id()
                self.employee_records['Role title'] = 'Manager'
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = float(input('Salary: '))
                self.employee_records['Department name'] = input('Department name: ')
                self.employee_records['Direct reports number'] = input('Direct reports number: ')
                self.employee_records['Allowance rate'] = input('Allowance  rate: ')
                # Store employee records in a json file
                self.write_records_to_json('employee records.json')

            elif option == '3':
                print('Fill in the following:')
                employee_id = self.generate_employee_id()
                self.employee_records['Role title'] = 'Director'
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = float(input('Salary: '))
                self.employee_records['Department name'] = input('Department name: ')
                self.employee_records['Annual bonus'] = input('Annual bonus: ')
                # Store employee records in a json file
                self.write_records_to_json('employee records.json')

            elif option == '4':
                print('Fill in the following:')
                employee_id = self.generate_employee_id()
                self.employee_records['Role title'] = 'Intern'
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = float(input('Salary: '))
                self.employee_records['University name'] = input('University name: ')
                self.employee_records['Program name'] = input('Program name: ')
                self.employee_records['Program name'] = input('Internship duration: ')
                # Store employee records in a json file
                self.write_records_to_json('employee records.json')

            elif option == '5':
                break

            else:
                print('Incorrect choice. Enter the correct choice')
                continue

    #
    def update_employee_records(self):
        """
        Updates the records of the employee using the employee ID.
        return: none
        """

        # loading the dictionary of employee records
        employee_record = self.load_employee_record('employee records.json')
        employee_id = input("Enter the employee ID: ")
        employee_id_upper = employee_id.upper()

        if employee_id_upper in employee_record:
            record = employee_record[employee_id_upper]
                

            print('Employee Found. Please provide the updated information:\n')

            record['First name'] = input('First name: ')
            record['Last name'] = input('Last name: ')
            record['Email'] = input('Email: ')
            record['Telephone number'] = input('Telephone number: ')

            if record['Role title'] == 'Regular employee':
                record['Salary'] = float(input('Salary: '))

            elif record['Role title'] == 'Manager':
                record['Salary'] = float(input('Salary: '))
                record['Department name'] = input('Department name: ')
                record['Direct reports number'] = input('Direct reports number: ')
                record['Allowance rate'] = input('Allowance rate: ')

            elif record['Role title'] == 'Director':
                record['Salary'] = float(input('Salary: '))
                record['Department name'] = input('Department name: ')
                record['Annual bonus'] = input('Annual bonus: ')

            elif record['Role title'] == 'Intern':
                record['Salary'] = float(input('Salary: '))
                record['University name'] = input('University name: ')
                record['Program name'] = input('Program name: ')
                record['Program name'] = input('Internship duration: ')

            self.update_records_to_json(employee_record, 'employee records.json')
            print('Employee records updated successfully.')
            return
        print('Employee with ID', employee_id, 'not found.')

    
    def remove_employee_record(self):
        """This function read the employee records and remove the employee record.
           Based on the employee ID and the update the json file.

           return: None
        """
        # Load the dictionary of employee records
        employee_record = self.load_employee_record('employee records.json')
        employee_id = input("Enter the employee ID to remove: ")
        employee_id_upper = employee_id.upper()

        if employee_id_upper in employee_record:
            # Employee found, remove the record
            del employee_record[employee_id_upper]

            # Save the updated records to the JSON file
            self.update_records_to_json(employee_record, 'employee records.json')
            print('Employee record with ID', employee_id, 'has been removed.')
        else:
            print('Employee with ID', employee_id, 'not found.')
            

    def display_employee_records(self):
        """Display the well formated whole employee records.
           
           return: None
        """
        # Load the dictionary of employee records
        employee_record = self.load_employee_record('employee records.json')

        if not employee_record:
            print("No employee records found.")
            return

        # Create a PrettyTable with appropriate column headers
        table = PrettyTable()
        table.field_names = ["Employee ID", "Role title", "First name", "Last name", "Email",  "Salary",]

        for employee_id, record in employee_record.items():
            # Initialize the row with employee ID
            row = [employee_id]
            for field_name in table.field_names[1:]:
                row.append(record.get(field_name, "-"))  # If the field is not found, use "-"
            table.add_row(row)

        print(table)

    def store_attendance_data(self):
        """ The function that record attendance using record_attendance() function
            And it store it to the json file.
        
        """

        employee_record = self.load_employee_record('employee records.json')
        print('Please input the follow data to make attendance:\n')
        employee_id = input("The employee ID: ")

        if employee_id.upper() in employee_record:
            department = input("The Role title(ex: Manager): ")
            date = input("The date: ")
            in_time = input("The In time: ")
            out_time = input("The out time: ")

            # The creation of thr attendance parameter using attendance instance.      
            attendance = Attendance(employee_id, department, date, in_time, out_time)
            attendance_list = [attendance.record_attendance()]

            # Record the attendance to the json file
            self.dump_to_json_file('attendance record.json', attendance_list)

        else:
            print("This employee ID is not regitered, please add employee firstly.")
            return

    def calculate_worked_hours(self) -> float:
        """This function calculate the daily worked hours.

           return: float   
        """
        try:
        # Load the JSON file into the attendance_records dictionary
            with open('attendance record.json', 'r') as file:
                attendance_records = json.load(file)

        except FileNotFoundError:
            print("Error: File not found.")
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # Asking the employee ID and the period for calculating the working hours
        employee_id = input("Enter the employee ID to calculate the working hours: ")
        period = input("Enter the date(dd-mm-yyyy): ")

        # Loop out the dictionaries to check the employee ID and date
        for attendance in attendance_records:
            if attendance['Employee ID'] == employee_id.upper() and attendance['Date'] == period:

                    # Converting string into real date
                    in_time_converted = datetime.strptime(attendance['In time'], "%H:%M")
                    out_time_converted = datetime.strptime(attendance['Out time'], "%H:%M")
                    working_time = out_time_converted - in_time_converted  # in seconds
                    # Convert seconds to hours
                    working_hours = working_time.total_seconds() / 3600

                    return working_hours
                      
        print(f"There is no employee with ID: {employee_id} in attendance record on date {period}.")

    def display_employee_salary(self):
        """
        Displays employee salary records
        :return:
        """
        # Load employee records from json file
        try:
            with open('employee records.json', 'r') as json_file:
                employee_dict = json.load(json_file)
        except FileNotFoundError:
            print('File not found')
        print('Choose the role of the employee\n'
              '1. Regular employee\n'
              '2. Manager\n'
              '3. Director\n'
              '4. Intern\n'
              '5. Back\n'
              )
        option = input('Enter your choice: ')
        employee_objects = []
        for employee_id, employee_data in employee_dict.items():
            if option == '1' and employee_data['Role title'] == 'Regular employee':
                employee = Employee(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                )
                employee_objects.append(employee)
            elif option == '2' and employee_data['Role title'] == 'Manager':
                manager = Manager(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                    employee_data['Department name'],
                    employee_data['Direct reports number'],
                    employee_data['Allowance rate']

                )
                employee_objects.append(manager)
            elif option == '3' and employee_data['Role title'] == 'Director':
                director = Director(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                    employee_data['Department name'],
                    employee_data['Annual bonus']
                )
                employee_objects.append(director)
            elif option == '4' and employee_data['Role title'] == 'Intern':
                intern = Intern(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                    employee_data['University name'],
                    employee_data['Program name'],
                    employee_data['Internship duration']
                )
                employee_objects.append(intern)
            elif option == '4':
                exit()

        salary = Salary(0.3)
        salary_list = salary.display_monthly_salary(employee_objects)

    def generate_payslip(self):
        """
        Generate payslip of the employee
        :return: none
        """
        # Load employee records from json file
        try:
            with open('employee records.json', 'r') as json_file:
                employee_dict = json.load(json_file)
        except FileNotFoundError:
            print('File not found')
        identity = input('Enter ID of the employee: ')
        employee_objects = []
        for employee_id, employee_data in employee_dict.items():
            if employee_id == identity and employee_data['Role title'] == 'Regular employee':
                employee = Employee(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                )
                employee_objects.append(employee)
            elif employee_id == identity and employee_data['Role title'] == 'Manager':
                manager = Manager(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                    employee_data['Department name'],
                    employee_data['Direct reports number'],
                    employee_data['Allowance rate']

                )
                employee_objects.append(manager)
            elif employee_id == identity and employee_data['Role title'] == 'Director':
                director = Director(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                    employee_data['Department name'],
                    employee_data['Annual bonus']
                )
                employee_objects.append(director)
            elif employee_id == identity and employee_data['Role title'] == 'Intern':
                intern = Intern(
                    employee_id,
                    employee_data['First name'],
                    employee_data['Last name'],
                    employee_data['Email'],
                    employee_data['Telephone number'],
                    employee_data['Salary'],
                    employee_data['University name'],
                    employee_data['Program name'],
                    employee_data['Internship duration']
                )
                employee_objects.append(intern)

        salary = Salary(0.1)
        salary_list = salary.produce_payslip(employee_objects)




          
