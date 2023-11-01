# Human Resource Management Information System(HRMIS)

### System description

This system is a python program which manages activities and information of the employees 
using object-oriented programming. This system is composed of employee management, attendance tracking, 
salary calculation, reporting and data persistence for human resource management.

### Features

Our system has the following features:
1. **Employee management**: The system has function of adding, updating and removing the employee records.
2. **Attendance Tracking**: The system has function of recording employee attendance, displaying attendance
records and calculate the total working hours of each employee.
3. **Salary management**: The system has function of calculating and displaying monthly salaries of the
                         employees.
4. **Reporting**: The system has function of generating and displaying reports of employee list, attendance
summary and salary summary
5. **Data persistence**: The system has a function to save employee records, attendance data, and salary information
to json file.
6. **Exception handling**: The system ensure use of error handling to track potential program issues.
7. **USer Interface**: The system Implements command line interface for interacting with the system.

## Class Descriptions
The program consists of several classes, each serving a specific purpose:

**HRMIS**: This class manages employee records, attendance tracking, and salary calculations. 
It acts as the main controller for the HRMIS program.

**Attendance**: This class is responsible for recording and displaying attendance records, 
calculating working hours, and loading/saving attendance data from/to JSON files.

**Salary**: Manages salary information for each employee, including base salary, taxes, bonuses, 
and allowances. It calculates the monthly net salary for employees.

**Director, Manager, Intern, and Employee**: These classes represent different employee roles, 
each with its own attributes and methods related to salary and compensation. 
They are used to store employee-specific data and calculate role-specific salary components.

**TestHRMIS** : This class inherit the `unittest.TestCase` and import HRMIS to test its methods.

**TestAttendance**: This class inherit the `unittest.TestCase` and import attendance to test its methods.



### Inheritance Hierarchy Structure

The system has the following class:

* Employee: This is the class that represents an employee with their roles
* Attendance: This is the class that represents attendance records for each employee, including date, in-time,
and out-time.
* Salary: This is the class that represents salary information for each employee
* HRMIS: This is the class that represents the HR management system which inherits salary class and inheritance class.


### How to run


## Usage

Once you have opened the HRMIS run the file named **menu** , then use the following menu options:

### Employee Management

1. **Add employee records:** Add new employee records with details such as first name, last name, email, and more.

2. **Update employee records:** Update the details of existing employees using their employee ID.

3. **Remove employee records:** Delete employee records based on their employee ID.

4. **Back:** Return to the main menu.

### Attendance Tracking

1. **Make attendance records:** Record attendance for employees, including the date, in-time, and out-time.

2. **Display employee attendance records:** Display the attendance records for individual employees.

3. **Display team attendance records:** Display the attendance records for a specific department or team.

4. **Calculate the employee daily worked hours:** Calculate the worked hours for an employee on a specific date.

5. **Back:** Return to the main menu.

### Salary Management

1. **Display employee salary:** Display the salaries of employees.

2. **Generate payslip:** Generate payslips for employees.

3. **Back:** Return to the main menu.

### Reporting

1. **Display employee records:** Display employee records in a tabular format.

2. **Display attendance summary:** Display an attendance summary for all employees.

3. **Display salary summary:** Display a summary of employee salaries.

4. **Back:** Return to the main menu.


```python
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
```
To exit the HRMIS system, you can choose the "Exit" option from the main menu. This will gracefully exit the application.

## Unit Tests

In addition to the core features and functionality of HRMIS, we have included unit tests to ensure that the program's components work as expected. The unit tests are conducted using Python's `unittest` framework. 
### To run 

the testcase you just run the file named TestHrmis, TestAttendance, TestSalary. There are three file for testcase.

Here is an overview of the included unit tests:

### `TestHRMIS` class

This test suite focuses on the HRMIS class, responsible for managing employee records,
 attendance tracking, and salary calculations.

#### `test_add_employee_records`

This function tests the functionality of adding employee records. 
It simulates user input for adding a new employee and verifies that,
the employee record is correctly added to the system and saved in a JSON file.

#### `test_update_employee_records`

This function tests the update feature of employee records. 
It first adds a new employee record and then simulates user input to update the employee's details. 
The test verifies that the updated information is correctly stored in the system.

#### `test_remove_employee_record`

This function tests the removal of employee records. It adds an employee record,
 and then simulates user input to remove the employee. 
 The test ensures that the employee record is no longer present in the JSON file.

#### `test_calculate_worked_hours`

This function tests the calculation of worked hours for employees. 
It adds an employee record, records attendance data, and then calculates the worked hours. 
The test checks whether the calculated worked hours match the expected value.

### `TestAttendance` class

This test suite focuses on the Attendance class, responsible for recording and managing employee attendance data.

#### `test_record_attendance`

This function tests the `record_attendance` method. 
It checks if the method correctly generates a dictionary with attendance details,
 and ensures that the dictionary contains the expected keys and values.

#### `test_load_attendance_from_json`

This function tests the loading of attendance data from a JSON file. 
It first creates a temporary JSON file with test data, loads the data using the method, 
and checks if the loaded data matches the expected values.

#### `test_dump_to_json_file`

This function tests the appending of attendance data to a JSON file. 
It creates a temporary JSON file, appends additional data using the method, 
and verifies if the appended data is present in the updated file.

### `TestSalary` class

This test focuses on testing the functionality of two functions in Salary class.

#### `test_calculate_monthly_salary`

This test case checks if the `calculate_monthly_salary` method in the Salary class correctly calculates the net monthly salary of an employee after applying taxes.

#### `test_display_monthly_salary`

This test case verifies that the `display_monthly_salary` method in the Salary class generates the expected output when displaying monthly salary information for a list of employees.


## Dependencies
The program relies on the following external libraries:

**Pandas**: A Python library for data manipulation and analysis.

**PrettyTable**: A library for creating formatted text tables.

**Tabulate**: A library for creating text-based tables.

**unittest.TestCase**: A library for test case

## Database

Using Json file, created Attendance record file and employee records file to store and view the output.
Also we have the other file for testing attendance.