class Employee:
    count = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count += 1

    @staticmethod
    def average_salary(employees):
        return sum(emp.salary for emp in employees) / len(employees)

class FulltimeEmployee(Employee):
    pass

if __name__ == "__main__":
    e1 = Employee("John", "Doe", 50000, "IT")
    e2 = FulltimeEmployee("Jane", "Doe", 60000, "HR")
    print("Average Salary:", Employee.average_salary([e1, e2]))
