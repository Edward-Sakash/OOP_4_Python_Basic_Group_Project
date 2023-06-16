from task_1 import Person, Student, Teacher

# Create instances of Person, Student, and Teacher
person = Person("John Doe", 25)
student = Student("Jane Smith", 20, "S12345", 3.8)
teacher = Teacher("Mr. Johnson", 40, "T98765", "Mathematics")

# Print details of Person, Student, and Teacher
print("Person Details:")
person.print_details()
print("\nStudent Details:")
student.print_details()
print("\nTeacher Details:")
teacher.print_details()
