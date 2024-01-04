# WAP to create Employee Class
class Employee:
    def __init__(self, emp_id, emp_name, emp_gender, emp_city, emp_salary):
        self.id = emp_id
        self.name = emp_name
        self.gender = emp_gender
        self.city = emp_city
        self.salary = emp_salary
    def display_info(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"City: {self.city}")
        print(f"Salary: {self.salary}")
employee1 = Employee(1, "Pankaj", "Male", "Delhi", 55000)
employee1.display_info()



















