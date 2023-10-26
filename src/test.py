from salary import Salary
from director import Director
from manager import Manager

director = Director('456', 'Leah', 'Uwineza',
                    'leahuwi@gmail.com', '+250789596293',
                    '234-345-6543', 13000, 'Finance',
                    2000,20,100)
# manager = Manager('321', 'Calvin', 'Ishimwe',
#                       'calvinira@gmail.com', '+250780424178',
#                       '077-5689-65', 10000, 'Marketing',
#                       5, 50,
# #                       20, 100)
director_salary = Salary(0.3)
print(director_salary.display_salary(director))










