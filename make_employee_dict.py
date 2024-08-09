class Employee:
    def __init__(self, name: str, id: str, salary: float, email: str):
        self.__name = name
        self.__id = id
        self.__salary = salary
        self.__email = email

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__id

    def get_salary(self):
        return self.__salary

    def get_email_address(self):
        return self.__email

    def __str__(self):
        return "name: " + self.__name + "\nID: " + self.__id + "\nSalary: " + str(self.__salary) + "\nEmail: " + self.__email

def make_employee_dict(names, IDs, salaries, emails):
    employee_dict = {}
    for i in range(len(names)):
        employee_dict[IDs[i]] = Employee(names[i], IDs[i], salaries[i], emails[i])
    return employee_dict

