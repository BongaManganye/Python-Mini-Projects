class  Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number


owner1 = Owner("Danny", "30077 Matsikitsane", "0635811543")
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
print(dog1.owner.name)

owner2 = Owner("Sally", "2004 Tsakani view", "079599000")
dog2 = Dog("Bonga", "Greyhound", owner2)
print(dog2.owner.name)
