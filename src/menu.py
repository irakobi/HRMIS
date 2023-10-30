from HRMIS import HRMIS


def employee_management():
    """
    Displays employment management menu
    return: none
    """
    print('1. Add employee records\n'
          '2. Update employee records\n'
          '3. Remove employee records\n'
          '4. Exit'
          )
    hrms = HRMIS()
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            hrms.add_employee_records()
        elif option == '2':
            hrms.update_employee_records()
        elif option == '3':
            hrms.remove_employee_records()
        elif option == '4':
            exit()
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def attendance_tracking():
    """
    Displays attendance tracking menu
    return: none
    """
    print('1. Record attendance records\n'
          '2. Display attendance records\n'
          '3. Exit'
          )
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            record_attendance()
        elif option == '2':
            display_attendance()
        elif option == '3':
            exit()
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def salary_management():
    """
    Displays salary management menu
    return: none
    """
    print('1. Display employee salary\n'
          '2. Generate payslip\n'
          '3. Exit'
          )
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            display_employee_salary()
        elif option == '2':
            generate_payslip()
        elif option == '3':
            exit()
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def reporting():
    """
    Display reporting menu
    return: none
    """
    print('1. Display employee list\n'
          '2. Display attendance summary\n'
          '3. Display salary summary\n'
          '4. Exit'
          )
    while True:
        option = input('Enter your choice: ')
        # Check for the option and call the function
        if option == '1':
            display_employee_list()
        elif option == '2':
            display_attendance_summary()
        elif option == '3':
            display_salary_summary()
        elif option == '4':
            exit()
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


def main():
    """
    Provides command line interface for the HR manager.
    :return:
    """
    print('Welcome to the HRM-IS menu\n'
          '--------------------------\n\n'
          'Menu options:\n'
          '1. Employee management\n'
          '2. Attendance tracking\n'
          '3. Salary management\n'
          '4. Reporting\n'
          '5. Exit'
          )
    while True:
        option = input('Enter your choice: ')
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
            exit()
        else:
            print('Incorrect choice. Enter the correct choice')
            continue


main()
