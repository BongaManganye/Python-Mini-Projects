#Using what we learned with functions, modify the Television class constructor so that
#channel_min and channel_max are optional parameters, where channel_min
#defaults to 2 and channel_max defaults to 14

class Television:
    def __init__(self, min=2, max=14 ):
        self.powered = False
        self.channel = min
        self.min_channel = min
        self.max_channel = max

    def channel_down(self):
        if self.channel - 1 >= self.min_channel:
            self.channel -= 1
        else:
            self.channel = self.max_channel

    def channel_up(self):
        if self.channel + 1 <= self.max_channel:
            self.channel += 1
        else:
            self.channel = self.min_channel

tv = Television()
tv.channel_down()
print(tv.channel)
tv.channel_up()
print(tv.channel)
