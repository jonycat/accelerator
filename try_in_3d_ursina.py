from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *


app = Ursina()



class Ground(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'plane',
            texture = "grass",
            scale = 500,
            position = Vec3(0, 0, 0),
            collider = 'plane')




class Enemy(Entity):
    def __init__(self):
        super().__init__(parent = scene,
                         model = 'cube',
                         texture = 'color',
                         scale = 5,
                         position = (10,2.5,0),collider = "box")



pickup = Entity(model="sphere", position=(1,.5,3))


def Game_over():
    Gameover = Entity(model='quad', parent=camera.ui, scale=(2, 1), texture='color')

def Ambient():
    pass



def Screamer():
    video_player = Entity(model='quad', parent=camera.ui, scale= (2,1), texture='video.mp4')
    a = audio.Audio(sound_file_name='sound.mp3', loop=False)




player = FirstPersonController(has_pickup = False)
ground = Ground()
Sky()
Enemy()



def update():

    if not player.has_pickup and distance(player, pickup) < pickup.scale_x:


        player.has_pickup = True
        pickup.animate_scale(0,duration=.1)
        destroy(pickup,delay=.1)
        Screamer()




app.run()