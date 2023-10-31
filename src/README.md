# Human Resource Management Information System(HRMIS)

### System description

This system is a python program which manages activities and information of the employees 
using object-oriented programming. This system is composed of employee management, attendance tracking, 
salary calculation, reporting, data persistence and error handling for human resource management.

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

### Inheritance Hierarchy Structure

The system has the following class:

* Employee: This is the class that represents an employee with their roles
* Attendance: This is the class that represents attendance records for each employee, including date, in-time,
and out-time.
* Salary: This is the class that represents salary information for each employee
* HRMIS: This is the class that represents the HR management system which inherits salary class and inheritance class.

### How to run

