# Part 1: Design Your Own Class - Smartphone

# Smartphone class with attributes and methods
class Smartphone:
    # Constructor to initialize the object with specific attributes
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    # Method to make a call
    def make_call(self, contact):
        print(f"Calling {contact}...")

    # Method to send a message
    def send_message(self, contact, message):
        print(f"Sending message to {contact}: '{message}'")

    # Method to check the battery level
    def check_battery(self):
        print(f"Battery at {self.battery_percentage}%")

    # Method to charge the phone
    def charge(self):
        self.battery_percentage = 100
        print("Phone is fully charged!")


# Create an instance of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 13", 45)

# Test the methods of the Smartphone class
my_phone.make_call("John")
my_phone.send_message("Jane", "Hello, how are you?")
my_phone.check_battery()
my_phone.charge()


# Part 2: Polymorphism Challenge - Vehicles

# Base class representing a generic Vehicle
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Test the polymorphism by creating instances of each vehicle and calling move()
car = Car()
plane = Plane()
boat = Boat()

car.move()  # Output: Driving 🚗
plane.move()  # Output: Flying ✈️
boat.move()  # Output: Sailing 🚤


# Part 3: Inheritance Layer with SmartphoneWithCamera

# Subclass extending Smartphone to include camera functionality
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, camera_quality):
        super().__init__(brand, model, battery_percentage)  # Call the parent constructor
        self.camera_quality = camera_quality  # Add a new attribute for camera quality

    # Method to take a photo
    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} camera quality.")


# Create an instance of SmartphoneWithCamera
my_camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 60, "108MP")

# Test the methods from the parent and the subclass
my_camera_phone.make_call("Alice")
my_camera_phone.send_message("Bob", "Check out my new phone!")
my_camera_phone.take_photo()
my_camera_phone.check_battery()
