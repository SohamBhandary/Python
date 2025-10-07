# Parent class
class Chai:
    def __init__(self, type_):
        self.type = type_

    def describe(self):
        print(f"This is {self.type} chai.")

# Child class
class GingerChai(Chai):
    def __init__(self, type_, spice_level):
        super().__init__(type_)  # Call parent constructor
        self.spice_level = spice_level

    def describe(self):
        super().describe()  # Call parent method
        print(f"Spice level: {self.spice_level}")

# Usage
regular = Chai("Regular")
ginger = GingerChai("Ginger", "High")

regular.describe()
print("---")
ginger.describe()
