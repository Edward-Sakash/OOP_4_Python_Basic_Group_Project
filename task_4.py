class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def get_salary(self):
        return self.salary

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, emp_id, team_size, base_salary, bonus):
        super().__init__(name, emp_id, 0)
        self.team_size = team_size
        self.base_salary = base_salary
        self.bonus = bonus
        self.calc_salary()

    def calc_salary(self):
        self.salary = self.base_salary + (self.team_size * self.bonus)


class Clerk(Employee):
    def __init__(self, name, emp_id, hourly_wage, num_hours):
        super().__init__(name, emp_id, 0)
        self.hourly_wage = hourly_wage
        self.num_hours = num_hours
        self.calc_salary()

    def calc_salary(self):
        self.salary = self.hourly_wage * self.num_hours
