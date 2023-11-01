# Import modules
import os
from HRMIS import HRMIS

# create HRMIS object
hr_manager = HRMIS()


def clear_screen():
    """
    Clears the console scree
    return: none
    """
    os.system('cls')


def employee_management():
    """
    Displays employment management menu, and perform chosen task.
    return: none
    """
    print('Choose option\n\n'
          '1. Add employee records\n'
          '2. Update employee records\n'
          '3. Remove employee records\n'
          '4. Back\n'
          )
    while True:
        option = input('Enter your choice: ')  # request for the option
        clear_screen()
        # Check for the option and call the function to perform the task
        if option == '1':
            hr_manager.add_employee_records()
        elif option == '2':
            hr_manager.update_employee_records()
        elif option == '3':
            hr_manager.remove_employee_record()
        elif option == '4':
            print('WELCOME TO HRMIS \n'
                  '----------------\n\n'
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
    Displays attendance tracking menu and perform chosen operations.
    return: none
    """
    print('Choose the option\n\n'
          '1. Make attendance records\n'
          '2. Display employee attendance records\n'
          '3. Display team attendance records\n'
          '4. Calculate employee daily worked hours\n'
          '5. Back\n'
          )
    while True:
        option = input('Enter your choice: ')  # request for the option
        clear_screen()
        # Check for the option and call the function to perform the task
        if option == '1':
            hr_manager.store_attendance_data()
        elif option == '2':
            hr_manager.display_employee_attendance()
        elif option == '3':
            hr_manager.display_team_attendance()
        elif option == '4':
            print(f"The worked hours: {hr_manager.calculate_worked_hours()}")
        elif option == '5':
            print('WELCOME TO HRMIS\n'
                  '----------------\n\n'
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
    Displays salary management menu and perform chosen operations.
    return: none
    """
    print('Salary Management\n\n'
          '1. Display employee salary\n'
          '2. Generate payslip\n'
          '3. Back\n'
          )
    while True:
        option = input('Enter your choice: ')  # request the option
        clear_screen()
        # Check for the option and call the function
        if option == '1':
            hr_manager.display_employee_salary()
        elif option == '2':
            hr_manager.generate_payslip()
        elif option == '3':
            print('WELCOME TO HRMIS\n'
                  '----------------\n\n'
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
    Generate and display reporting menu for employee, attendance and Salary
    from the database(json file).
    return: none
    """
    print('Choose the option\n\n'
          '1. Display employee records\n'
          '2. Display attendance summary\n'
          '3. Display salary summary\n'
          '4. Back'
          )
    while True:
        option = input('Enter your choice: ')  # request for option
        clear_screen()
        # Check for the option and call the function and perform the task
        if option == '1':
            hr_manager.display_employee_records()
        elif option == '2':
            hr_manager.display_attendance_summary()
        elif option == '3':
            hr_manager.display_salary_summary()
        elif option == '4':
            print('WELCOME TO HRMIS\n'
                  '----------------\n\n'
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
    print('WELCOME TO HRMIS\n'
          '----------------\n\n'
          'Menu options:\n'
          '1. Employee management\n'
          '2. Attendance tracking\n'
          '3. Salary management\n'
          '4. Reporting\n'
          '5. Exit\n'
          )
    while True:
        option = input('Enter your choice: ')  # request option
        clear_screen()
        # Check for the option and call the function to perform task
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
