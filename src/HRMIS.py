import json


class HRMIS:
    """
    This module  represents the HR management system, which manages employee
    records, attendance, and salary calculations.
    """
    def __init__(self):
        # create a dictionary to store employee records
        self.employee_records = {}
        self.records = [self.employee_records]

    def add_employee_records(self):
        """
        Adds records of the employee
        return: none
        """
        print('Choose the employee role\n\n'
              '1. Regular employee\n'
              '2. Manager\n'
              '3. Director\n'
              '4. Intern\n'
              '5. Exit')
        while True:
            option = input('Enter your choice: ')
            # Check for the option and perform required task
            if option == '1':
                print('Fill in the following:')
                self.employee_records['Employee ID'] = input('Employee ID: ')
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = input('Salary: ')

                # Load data from the file
                try:
                    with open('Regular employee records.json', 'r') as file:
                        loaded_data = json.load(file)
                except FileNotFoundError:
                    loaded_data = []
                self.records.append(self.employee_records)
                # Store employee records in a json file
                try:
                    with open('Regular employee records.json', 'a') as file:
                        json.dump(self.records, file, indent=4)
                        file.write('\n')
                    print('Employee records added successfully')
                except FileNotFoundError:
                    print('File not found')
                break

            elif option == '2':
                print('Fill in the following:')
                self.employee_records['Employee ID'] = input('Employee ID: ')
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = input('Salary: ')
                self.employee_records['Department name'] = input('Department name: ')
                self.employee_records['Direct reports number'] = input('Direct reports number: ')
                self.employee_records['Allowance rate'] = input('Allowance  rate: ')
                # Store employee records in a json file
                try:
                    with open('Manager records.json', 'a') as file:
                        json.dump(self.employee_records, file, indent=4)
                    print('Employee records added successfully')
                except FileNotFoundError:
                    print('File not found')
                break

            elif option == '3':
                print('Fill in the following:')
                self.employee_records['Employee ID'] = input('Employee ID: ')
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = input('Salary: ')
                self.employee_records['Department name'] = input('Department name: ')
                self.employee_records['Annual bonus'] = input('Annual bonus: ')
                # Store employee records in a json file
                try:
                    with open('Director records.json', 'a') as file:
                        json.dump(self.employee_records, file, indent=4)
                    print('Employee records added successfully')
                except FileNotFoundError:
                    print('File not found')
                break

            elif option == '4':
                print('Fill in the following:')
                self.employee_records['Employee ID'] = input('Employee ID: ')
                self.employee_records['First name'] = input('First name: ')
                self.employee_records['Last name'] = input('Last name: ')
                self.employee_records['Email'] = input('Email: ')
                self.employee_records['Telephone number'] = input('Telephone number: ')
                self.employee_records['Salary'] = input('Salary: ')
                self.employee_records['University name'] = input('University name: ')
                self.employee_records['Program name'] = input('Program name: ')
                # Store employee records in a json file
                try:
                    with open('Intern records.json', 'a') as file:
                        json.dump(self.employee_records, file, indent=4)
                    print('Employee records added successfully')
                except FileNotFoundError:
                    print('File not found')
                break

            elif option == '5':
                exit()

            else:
                print('Incorrect choice. Enter the correct choice')
                continue

    #
    # def update_employee_records(self, employee_id):
    #     """
    #     Updates the records of the employee.
    #     return: none
    #     """
    #     if employee_id in self.employee_records:
    #

hrmis = HRMIS()
hrmis.add_employee_records()
