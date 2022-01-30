from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
app = Ursina()
#
class Ground(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'plane',
            texture = "grass",
            scale = 500,
            position = Vec3(0, 0, 0),
            collider = 'plane')


player = FirstPersonController(model='cube',
                            texture = "None",
                            scale=0.75,
                            collider = 'box',
                              speed = 2.255)
camera.z = -5
ground = Ground()



app.run()