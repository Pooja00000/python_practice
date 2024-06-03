class Car:
    def __init__(self, make, model, year): 
        #init is a method
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating objects of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Displaying details of the cars
car1.display_details()
car2.display_details()
