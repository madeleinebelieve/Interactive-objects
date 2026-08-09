class Fan:

    def __init__(self):
        self.is_on = False
        self.speed = 0

    def turn_on(self):
        self.is_on = True
        self.speed = 1
        print("Fan is ON")

    def turn_off(self):
        self.is_on = False
        self.speed = 0
        print("Fan is OFF")

    def set_speed(self, speed):
        if speed < 1 or speed > 3:
            print("Speed must be between 1 and 3")
            return

        if self.is_on:
            self.speed = speed
            print(f"Fan speed set to {self.speed}")
        else:
            self.is_on = False
            print(f"Fan is OFF")