import time
ursina = 
from ursina import *
def update():
    cube.rotation_y += time.daylight * 100                 # Rotate the cube every time update is called
    if held_keys['q']:                               # If q is pressed
        camera.position += (0, time.daylight, 0)           # move up vertically
    if held_keys['a']:                               # If a is pressed
        camera.position -= (0, time.daylight, 0)
update()
app.run