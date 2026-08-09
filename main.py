from fan import Fan
from blender_controller import BlenderFanController

fan = Fan()
controller = BlenderFanController()

fan.turn_on()
controller.start_blades()

fan.turn_off()
controller.stop_blades()