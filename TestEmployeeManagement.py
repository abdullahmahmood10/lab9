import unittest
import EmployeeManagement as EmpManagement

class TestEmployeeManagement(unittest.TestCase):
    def test_add_employee(self):
        management = EmpManagement.EmployeeManagement()
        employee = EmpManagement.Employee("John Doe", 25, 6666,'IT')
        management.add_employee(employee)
        self.assertIn(employee, management.employees) 

    def test_show_employee(self):
        management = EmpManagement.EmployeeManagement()
        employee1 = EmpManagement.Employee("John Doe", 25, 6666,'IT')
        employee2 = EmpManagement.Employee("Abdullah", 22, 6667,'HR')
        management.add_employee(employee1)
        management.add_employee(employee2)
        expected_output = "Name: John Doe, Age: 25, id: 6666, department: IT"
        self.assertEqual(expected_output, management.show_employee(6666))

    def test_delete_student(self):
        management = EmpManagement.EmployeeManagement()
        employee1 = EmpManagement.Employee("John Doe", 25, 6666,'IT')
        employee2 = EmpManagement.Employee("Abdullah", 22, 6667,'HR')
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.delete_employee(6667)
        self.assertNotIn(employee2, management.employees)

    def test_add_employee_1(self):
        management = EmpManagement.EmployeeManagement()
        employee1 = EmpManagement.Employee("John Doe", 25, 6666,'IT')
        employee2 = EmpManagement.Employee("Abdullah", 22, 6666,'HR')
        management.add_employee(employee1)
        with self.assertRaises(Exception):
            management.add_employee(employee2)

    def test_delete_student_1(self):
        management = EmpManagement.EmployeeManagement()
        employee1 = EmpManagement.Employee("John Doe", 25, 6666,'IT')
        management.add_employee(employee1)
        with self.assertRaises(Exception):
            management.delete_employee(6555)

    def test_add_employee_2(self):
        management = EmpManagement.EmployeeManagement()
        employee1 = EmpManagement.Employee("John Doe", 25, 6666,'')
        with self.assertRaises(Exception):
            management.add_employee(employee1)

if __name__ == "__main__":
    test_employee = TestEmployeeManagement()
