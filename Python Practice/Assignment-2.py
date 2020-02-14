class Company:                      

    __count=0                       

    @classmethod
    def display_count(cls):              
        cls.__count = cls.__count+1
        return cls.__count

    @staticmethod
    def location():          
        Company._location = "Bangalore"
        return Company._location
    
    def gross_calc(self, basic_pay):        
        gross_salary = basic_pay + (10 * basic_pay) / 100 + (12 * basic_pay) / 100
        return gross_salary
    
    
class Employee(Company):             

    def __init__(self, name = "", id = 0):
        self.id = id
        self.name = name
    
    def display(self, basic_pay):
        print("ID : ", self.id)
        print("Name : ", self.name)
        print("Company Location : ", self.location())       
        print("Count : ", self.display_count())
        print("Gross Salary : ", self.gross_calc(basic_pay))

basic_pay = int(input("Enter the Basic Pay : "))
emp = Employee("Ajay",7)            
emp.display(basic_pay) 

#=======================o/p======================================

Enter the Basic Pay : 22000                                                                                                                              
ID :  7                                                                                                                                                  
Name :  Ajay                                                                                                                                             
Company Location :  Bangalore                                                                                                                            
Count :  1                                                                                                                                               
Gross Salary :  26840.0

#**************************************************************************************************
