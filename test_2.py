from task_2 import Vehicle, Car, Bike

# Create instances of Vehicle, Car, and Bike
vehicle = Vehicle("1234ABCD", 4, "1000cc", "X5", "BMW")
car = Car("5678WXYZ", "2000cc", "Civic", "Honda")
bike = Bike("9ABCDEFG", "150cc", "Ninja", "Kawasaki")

# Print details of Vehicle, Car, and Bike
print("Vehicle Details:")
vehicle.print_details()
print("\nCar Details:")
car.print_details()
print("\nBike Details:")
bike.print_details()
