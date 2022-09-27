#Write a class named Employee that holds the following data about an employee in attributes: name, ID number, department, job title and monthly salary.The Employee class’s __init__ method should accept an argument for each attribute. The Employee class should have accessor methods for each attribute. All attribute should be hidden.

class Employee:
    def __init__ (self, name, id, department, title, salary):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title
        self.__salary = salary
    
    def set_name(self, name):
        self.__name = name
    
    def set_id(self, id):
        self.__id = id
    
    def set_department(self, department):
        self.__department = department
    
    def set_title(self, title):
        self.__title = title
    
    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_department(self):
        return self.__department
    def get_title(self):
        return self.__title
    def get_salary (self):
        return self.__salary

    def __str__(self):
        return "Name: " + self.__name + "\nID Number: " + self.__id + "\nDepartment: " + self.__department + '\nTitle: ' + self.__title + 'Monthly Salary: ' + self.__salary 
        