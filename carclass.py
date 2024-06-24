class Vehicle:
    def __init__(self):
        self.vehicleType = "car" #There is only a car, no broomsticks here!

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__()
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def getDetails():
    
    year = input("Enter the year of your car ")
    make = input("Enter the make of your car ")
    model = input("Enter the model of your car ")
    doors = input("Enter the number of doors for your car (2 or 4) ")
    roof = input("Enter the type of roof (solid or sun roof) ")

    car = Automobile(year, make, model, doors, roof)
    return car

def displayDetails(car):
    print("\nCar Details")
    print(f"Vehicle Type: {car.vehicleType}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

def main():
    car = getDetails()
    displayDetails(car)

if __name__ == "__main__":
    main()