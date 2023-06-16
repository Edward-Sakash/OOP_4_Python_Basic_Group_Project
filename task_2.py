class Vehicle:
    def __init__(self, reg_num, num_wheels, engine_power, model, make):
        self.reg_num = reg_num
        self.num_wheels = num_wheels
        self.engine_power = engine_power
        self.model = model
        self.make = make

    def print_details(self):
        print(f"Registration Number: {self.reg_num}")
        print(f"Number of Wheels: {self.num_wheels}")
        print(f"Engine Power: {self.engine_power}")
        print(f"Model: {self.model}")
        print(f"Make: {self.make}")


class Car(Vehicle):
    def __init__(self, reg_num, engine_power, model, make):
        super().__init__(reg_num, 4, engine_power, model, make)


class Bike(Vehicle):
    def __init__(self, reg_num, engine_power, model, make):
        super().__init__(reg_num, 2, engine_power, model, make)
