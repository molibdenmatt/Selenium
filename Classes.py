class Pies:

    gatunek = 'Pies domowy'

    def __init__(self, breed, name, age):
        print("Inside of the init method")
        self.breed = breed
        self.name = name
        self.age = age

    def bark(self):
        return "Woof! Woof!"

    def present_dog(self):
        print("Breed: " + self.breed)
        print("Name: " + self.name)
        print("Age: " + str(self.age))

reksio = Pies('Mongrel', 'Reksio', 2)

print(reksio.age)
reksio.age = 3
print(reksio.age)

print(reksio.name)
print(reksio.breed)

reksio.gatunek = "Ptak"
print(reksio.gatunek)
print(Pies.gatunek)

print(reksio.bark())
reksio.present_dog()

