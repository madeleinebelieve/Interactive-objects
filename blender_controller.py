import bpy

class BlenderFanController:
    def __init__(self, blades_object_name):
        self.blades_object_name = blades_object_name
        self.is_spinning = False

    def get_blades(self):
        return bpy.data.objects.get(self.blades_object_name)

    def rotate_blades(self, angle):
        blades = self.get_blades()

        if blades is None:
            print(f"Object '{self.blades_object_name}' not found")
            return

        blades.rotation_euler.y += angle

    def update_rotation(self):
        if not self.is_spinning:
            return None

        self.rotate_blades(0.1)

        return 0.02

    def start_blades(self):
        self.is_spinning = True
        bpy.app.timers.register(self.update_rotation)

    def stop_blades(self):
        self.is_spinning = False