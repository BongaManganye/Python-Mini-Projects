#Currently, the Television class initializes the channel with 2. Modify the Television
#class to receive the initial channel in its constructor as an optional parameter.

class Television:
    def __init__(self, initial_channel, min, max):
        self.powered = False
        self.channel = initial_channel
        self.min_channel = min
        self.max_channel = max

    def channel_down(self):
        if self.channel - 1 >= self.min_channel:
            self.channel -= 1

    def channel_up(self):
        if self.channel + 1 <= self.max_channel:
            self.channel += 1

tv = Television(6, 1, 99)

print(tv.channel)
