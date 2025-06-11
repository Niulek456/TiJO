from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Device):
    def turn_on(self):
        print("Light is on")

class Fan(Device):
    def turn_on(self):
        print("Fan is spinning")

class Button:
    def __init__(self, device: Device):
        self.device = device

    def press(self):
        self.device.turn_on()

# Użycie
light_button = Button(Light())
fan_button = Button(Fan())

light_button.press()
fan_button.press()
