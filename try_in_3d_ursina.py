from ursina.prefabs.first_person_controller import FirstPersonController

from ursina import *


app = Ursina()


Ambient_sound = True



level = load_model('map')
t = time.time()
Entity(model=level, collider=level, collision=True, scale=5, texture='grass')


enemy = Entity(model="bonnie.obj",texture='texture.png', position=(1,.5,3))


def Game_over():
    pass

def footsteps():
    pass


def Ambient():
    global Ambient_sound
    if Ambient_sound == True:
        ambient = audio.Audio(sound_file_name='Ambient.mp3', loop=True)

def sky():
    sky_model = Entity(model="quad",rotation_x=270, texture='brick', position=(0,100,0), scale=600)



def Screamer():

    Screamer_video= Entity(model='quad', parent=camera.ui, scale= (2,1), texture='video.mp4')
    a = audio.Audio(sound_file_name='sound.mp3', loop=True)



player = FirstPersonController()
player.speed = 7
#Ambient()
sky()


def update():
    if distance(player, enemy) < enemy.scale_x:
        enemy.animate_scale(1,duration=.1)
        Screamer()
        player.position=(0, 0, 0)
        Game_over()



    if held_keys['shift']:
        player.speed = 15
    else:
        player.speed = 7


app.run()