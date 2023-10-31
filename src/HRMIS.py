import json
import random
import string
from attendance import Attendance
# from salary import Salary
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
            print('Employee records added successfully')

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
                self.employee_records['Salary'] = input('Salary: ')

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
                self.employee_records['Salary'] = input('Salary: ')
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
                self.employee_records['Salary'] = input('Salary: ')
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
                self.employee_records['Salary'] = input('Salary: ')
                self.employee_records['University name'] = input('University name: ')
                self.employee_records['Program name'] = input('Program name: ')
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

        for record in employee_record:

            if record.get('Employee ID') == employee_id_upper:

                print('Employee Found. Please provide the updated information:\n')

                record['First name'] = input('First name: ')
                record['Last name'] = input('Last name: ')
                record['Email'] = input('Email: ')
                record['Telephone number'] = input('Telephone number: ')

                if record['Role title'] == 'Regular employee':
                    record['Salary'] = input('Salary: ')

                elif record['Role title'] == 'Manager':
                    record['Salary'] = input('Salary: ')
                    record['Department name'] = input('Department name: ')
                    record['Direct reports number'] = input('Direct reports number: ')
                    record['Allowance rate'] = input('Allowance rate: ')

                elif record['Role title'] == 'Director':
                    record['Salary'] = input('Salary: ')
                    record['Department name'] = input('Department name: ')
                    record['Annual bonus'] = input('Annual bonus: ')

                elif record['Role title'] == 'Intern':
                    record['Salary'] = input('Salary: ')
                    record['University name'] = input('University name: ')
                    record['Program name'] = input('Program name: ')

                self.update_records_to_json(employee_record, 'employee_records.json')
                print('Employee records updated successfully.')
                return
        print('Employee with ID', employee_id, 'not found.')
            
    
if __name__ == "__main__":
    hr = HRMIS()
    hr.update_employee_records()