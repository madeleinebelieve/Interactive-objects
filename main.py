class Fan:

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Fan is ON")

    def turn_off(self):
        self.is_on = False
        print("Fan is OFF")

fan = Fan()
print(fan.is_on)
fan.turn_on()
print(fan.is_on)
fan.turn_off()
print(fan.is_on)