import os
from HRMIS import HRMIS



hr_manager = HRMIS()

def clear_screen():
    os.system('cls')

def employee_management():
    """
    Displays employment management menu, and perform chosed operations.
    return: none
    """
    print('1. Add employee records\n'
          '2. Update employee records\n'
          '3. Remove employee records\n'
          '4. Back\n'
          )
    
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            hr_manager.add_employee_records()
        elif option == '2':
            hr_manager.update_employee_records()
        elif option == '3':
            hr_manager.remove_employee_record()
        elif option == '4':
            print('WELCOME TO HRMI SYSTEM FOR STARTUP\n'
            '--------------------------\n\n'
            'Menu options:\n'
            '1. Employee management\n'
            '2. Attendance tracking\n'
            '3. Salary management\n'
            '4. Reporting\n'
            '5. Exit\n'
            )
            break
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def attendance_tracking():
    """
    Displays attendance tracking menu and perfom chosed operations.
    return: none
    """
    print('1. Make attendance records\n'
          '2. Display employee attendance records\n'
          '3. Display team attendance records\n'
          '4. Calculate the employee daily worked hours\n'
          '5. Back\n'
          )
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            hr_manager.store_attendance_data()
        elif option == '2':
            hr_manager.display_employee_attendance()
        elif option == '3':
            hr_manager.display_team_attendance()
        elif option == '4':
            hr_manager.calculate_worked_hours()
        elif option == '5':
            print('WELCOME TO HRMI SYSTEM FOR STARTUP\n'
            '--------------------------\n\n'
            'Menu options:\n'
            '1. Employee management\n'
            '2. Attendance tracking\n'
            '3. Salary management\n'
            '4. Reporting\n'
            '5. Exit\n'
            )
            break
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def salary_management():
    """
    Displays salary management menu and perform chosed operation.
    return: none
    """
    print('1. Display employee salary\n'
          '2. Generate payslip\n'
          '3. Back\n'
          )
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            hr_manager.display_employee_salary()
        elif option == '2':
            pass
            hr_manager.generate_payslip()
        elif option == '3':
            print('WELCOME TO HRMIS SYSTEM FOR STARTUP\n'
            '-----------------------------------\n\n'
            'Menu options:\n'
            '1. Employee management\n'
            '2. Attendance tracking\n'
            '3. Salary management\n'
            '4. Reporting\n'
            '5. Exit\n'
            )
            break
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def reporting():
    """
    Generate and display reporting menu for employee, attendance and Salary.
    from the database(json file).
    return: none
    """
    print('1. Display employee records\n'
          '2. Display attendance summary\n'
          '3. Display salary summary\n'
          '4. Back'
          )
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            hr_manager.display_employee_records()
        elif option == '2':
            hr_manager.display_attendance_summary()
        elif option == '3':
            pass
        elif option == '4':
            print('WELCOME TO HRMI SYSTEM FOR STARTUP\n'
            '--------------------------\n\n'
            'Menu options:\n'
            '1. Employee management\n'
            '2. Attendance tracking\n'
            '3. Salary management\n'
            '4. Reporting\n'
            '5. Exit\n'
            )
            break
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def main():
    """
    Provides command line interface for the HR manager.
    :return:
    """
    print('WELCOME TO HRMI SYSTEM FOR STARTUP\n'
          '--------------------------\n\n'
          'Menu options:\n'
          '1. Employee management\n'
          '2. Attendance tracking\n'
          '3. Salary management\n'
          '4. Reporting\n'
          '5. Exit\n'
          )
    while True:
        option = input('Enter your choice: ')
        clear_screen()
        # Check for the option and call the function
        if option == '1':
            employee_management()
        elif option == '2':
            attendance_tracking()
        elif option == '3':
            salary_management()
        elif option == '4':
            reporting()
        elif option == '5':
            print("Exiting.........")
            exit()
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


main()
