# Define the Appliance class
class Appliance:
  # Method turn_on for the Appliance class
  def turn_on(self):
    return 'Appliance is now on'

# Define the WashingMachine class inheriting from Appliance
class WashingMachine(Appliance):
  # Method turn_on overridden in WashingMachine class
  def turn_on(self):
    return 'Washing machine starts spinning'

# Define the Refrigerator class inheriting from Appliance
class Refrigerator(Appliance):
  # Method turn_on overridden in Refrigerator class
  def turn_on(self):
    return 'Refrigerator starts cooling'

# Define the Microwave class inheriting from Appliance
class Microwave(Appliance):
  # Method turn_on overridden in Microwave class
  def turn_on(self):
    return 'Microwave starts heating'

# Create instances of each class
appliance = Appliance()
washing_machine = WashingMachine()
refrigerator = Refrigerator()
microwave = Microwave()

# Demonstrating polymorphism
for appliance_obj in (appliance, washing_machine, refrigerator, microwave):
  # Call the turn_on method on each object
  print(appliance_obj.turn_on())
