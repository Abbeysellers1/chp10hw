#Write a class that represents a payroll deduction transaction. Each instance should have the description, date, charge amount and employee ID as attributes. The class’s __init__ method should accept an argument for each attribute. The class should have accessor methods for each attribute. All attribute should be hidden.


class Payroll:
    def __init__ (self, description, date, charge, id):
        self.__description = description
        self.__date = date
        self.__charge = charge
        self.__id = id
    
   # def set_description(self, description):
   #     self.__description = description
    
   # def set_date(self, date):
   #     self.__date = date
    
   # def set_charge(self, charge):
   #     self.__charge = charge
    
   # def set_id(self, id):
   #     self.__id = id
    

    def get_description(self):
        return self.__description
    def get_date(self):
        return self.__date
    def get_charge(self):
        return self.__charge
    def get_id(self):
        return self.__id

    def __str__(self):
        return "Description: " + self.__description + "Date: " + self.__date + "Charge Amount: " + self.__charge+ "Employee ID: " + self.__id
