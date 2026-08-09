import bpy

class BlenderFanController:
    def __init__(self, blades_object_name):
        self.blades_object_name = blades_object_name

    def get_blades(self):
        return bpy.data.objects.get(self.blades_object_name)

    def rotate_blades(self, angle):
        blades = self.get_blades()

        if blades is None:
            print(f"Object '{self.blades_object_name}' not found")
            return

        blades.rotation_euler.y += angle

    def start_blades(self):
        print("Blender: start blades")

    def stop_blades(self):
        print("Blender: stop blades")