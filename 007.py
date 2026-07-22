#Add size and brand attributes to the Television class. Create two Television objects
#and assign them different sizes and brands. Then, print the value of those attributes
#to confirm the independence of the values of each instance (object).

class Television:
    def __init__(self):
        self.powered = False
        self.channel = 2
        self.size = 20
        self.brand = "EastTiger"

tv = Television()
tv.size = 27
tv.brand = "DingDang"
living_room_tv = Television()
living_room_tv.size = 52
living_room_tv.brand = "Xangala"

print(f"tv size={tv.size} brand={tv.brand}")
print(f"living_room_tv size={living_room_tv.size} brand={living_room_tv.brand}")
