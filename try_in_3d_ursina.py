from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController




app = Ursina()



def cutscene():
    pass


def map():
    level = load_model('map')
    Entity(model=level, collider=level, collision=True, scale=5, texture='grass')

#models

#house
home_outside = Entity(model="home_outside_model",collider="home_outside_model",collision=True,texture='house_outside_texture', position=(100,0,0),scale=1,rotation_y=180,)




#enemy
enemy = Entity(model="bonnie.obj",texture='texture.png', position=(1,.5,3))
#Triggers
visible_triggers = True

Trigger_1 = Entity(model="sphere",visible=visible_triggers, scale=10,position=(75,.5,10))
Trigger_Guys = Entity(model="cube",visible=visible_triggers, scale_z=50,position=(50,.5,10))


def Game_over():
    game_over_screen = Entity(model='quad', parent=camera.ui, scale=(2,1), texture='Menu')



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
    if distance(player, Trigger_1) < Trigger_1.scale_x:
        player.position = (0, 0, 0)

    if distance(player, Trigger_Guys) < Trigger_Guys.scale_x:
        audio.Audio(sound_file_name='sound.mp3', loop=False)




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