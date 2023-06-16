from task_4 import Employee, Manager, Clerk

# Create instances of Employee, Manager, and Clerk
employee = Employee("John Doe", "E123", 5000)
manager = Manager("Jane Smith", "M456", 10, 5000, 1000)
clerk = Clerk("David Johnson", "C789", 20, 40)

# Print details of Employee, Manager, and Clerk
print("Employee Details:")
employee.print_details()
print(f"Salary: {employee.get_salary()}")
print()

print("Manager Details:")
manager.print_details()
print(f"Salary: {manager.get_salary()}")
print()

print("Clerk Details:")
clerk.print_details()
print(f"Salary: {clerk.get_salary()}")
