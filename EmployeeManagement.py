class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if employee.id == "" or employee.name == "" or employee.age == "" or employee.department == "":
            raise Exception("Empty input")
        for e in self.employees:
            if e.id == employee.id:
                raise Exception("Duplicate employee")
        self.employees.append(employee)
        
    def show_employee(self, id):
        for employee in self.employees:
            if (employee.id == id):
                return f"Name: {employee.name}, Age: {employee.age}, id: {employee.id}, department: {employee.department}"

    def delete_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee.id == id:
                del self.employees[i]
                break
        else:
            raise Exception("Employee not found")