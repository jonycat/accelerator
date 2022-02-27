from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController




app = Ursina()






def map():
    level = load_model('map')
    Entity(model=level, collider=level, collision=True, scale=5, texture='grass')

#models

#house
home_outside = Entity(model="home_outside_model",texture='house_outside_texture', position=(0,0,0),scale=1)
#enemy
enemy = Entity(model="bonnie.obj",texture='texture.png', position=(1,.5,3))


def Game_over():
    game_over_screen = Entity(model='quad', parent=camera.ui, scale=(2,1), texture='Menu')


def footsteps():
    pass


def Ambient():
    ambient = audio.Audio(sound_file_name='Ambient.mp3', loop=True)

def sky():
    sky_model = Entity(model="quad",rotation_x=270, texture='night_sky', position=(0,100,0), scale=10000)



def Screamer():
    Screamer_video= Entity(model='quad', parent=camera.ui, scale= (2,1), texture='video.mp4')
    a = audio.Audio(sound_file_name='sound.mp3', loop=False)


screamer_time = 2.3
player = FirstPersonController()
player.scale = 3
player.jump_height = 0
Sky()
map()




def update():
    if distance(player, enemy) < enemy.scale_x:
        Screamer()
        player.position=(0, 0, 0)

        invoke(Game_over, delay=screamer_time)
        invoke(Ambient, delay=screamer_time)




    if held_keys['shift']:
        player.speed = 20
    else:
        player.speed = 10


app.run()