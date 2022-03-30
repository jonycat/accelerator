from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
from ursina.shaders import *
from ursina.lights import PointLight

def map():
    level = load_model('map')
    Entity(model=level, collider=level, collision=True, scale=5, texture='grass')




def locations(): #Create environment
    home_outside = Entity(model="home_outside_model",
                      collider="home_outside_model",
                      collision=True,
                      texture='house_outside_texture',
                      position=(100,0,0),scale=1,
                      rotation_y=180)


    home_inside = Entity(model="house_inside",
                     collider="house_inside",
                     collision=True,
                     texture='brick',
                     position=(0,-100,-30),
                     scale=30,
                     rotation_y=180)


    home_inside_roof = Entity(model='plane',
                              texture='grass',
                              position=(0,-89,0),scale=90,
                              rotation_x=180)

    light_position=(0,20,10)
    Entity(model='sphere',position= light_position,scale=5,shader=lit_with_shadows_shader,color= (0,255,255, 1))

    DirectionalLight(position=light_position, shadows=True)


#temporary_enemy
enemy = Entity(model="bonnie.obj",texture='texture.png', position=(1,.5,3))

#temporary_Triggers
visible_triggers = True

Trigger_1 = Entity(model="sphere",visible=visible_triggers, scale=10,position=(75,.5,10))
Trigger_Guys = Entity(model="plane",visible=visible_triggers, scale_z=5,position=(50,.5,10))

#Trigger_Screamer
#settings
x = 30
y = 0
z = 0
scale_z = 5

x_idol, y_idol, z_idol = -25.3238, -98.2, -11.0422
x_amog, y_amog, z_amog = 29.2416, -98.2, 5.07941
x_hehe, y_hehe, z_hehe = 11.6294, -98.2, -14.7563
x_micro, y_micro, z_micro = 11.98, -99, 6.95575


Screamer_trigger_idol = Entity(model="plane",visible=visible_triggers, scale_z=scale_z,position=(x_idol, y_idol, z_idol))
Screamer_trigger_amog = Entity(model="plane",visible=visible_triggers, scale_z=scale_z,position=(x_amog, y_amog, z_amog))
Screamer_trigger_hehe = Entity(model="plane",visible=visible_triggers, scale_z=scale_z,position=(x_hehe, y_hehe, z_hehe))
Screamer_trigger_micro = Entity(model="plane",visible=visible_triggers, scale_z=scale_z,position=(x_micro, y_micro, z_micro))




def Game_over():
    game_over_screen = Entity(model='quad', parent=camera.ui, scale=(2,1), texture='Menu')



def Ambient():
    ambient = audio.Audio(sound_file_name='Ambient.mp3', loop=True)

def sky():
    sky_model = Entity(model="quad",rotation_x=270, texture='night_sky', position=(0,100,0), scale=10000)



def Test_Screamer():
    Screamer_video= Entity(model='quad', parent=camera.ui, scale= (2,1), texture='video.mp4')
    a = audio.Audio(sound_file_name='sound.mp3', loop=False)

def Screamer(x,y,z, rotate, scale, screamer_vid, screamer_sound):
    Entity(model='quad', scale= (scale), texture=screamer_vid,position=(x,y,z), rotation_y=rotate, loop=False)
    a = audio.Audio(sound_file_name=screamer_sound, loop=False)
    screamer_time = 2



screamer_time = 2.3
player = FirstPersonController()

player.scale = 3
player.jump_height = 20
Sky()
map()
locations()


def update():
    if distance(player, Trigger_1) < Trigger_1.scale_x:
        player.position = (0, -99, 0)

    if distance(player, Screamer_trigger_idol) < Screamer_trigger_idol.scale_x:
        Screamer(x_idol, y_idol + 5, z_idol - 10, 180, 10, 'idol.mp4', 'idol.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_idol.position = (0, 100, 0)

    if distance(player, Screamer_trigger_amog) < Screamer_trigger_amog.scale_x:
        Screamer(x_amog, y_amog + 5, z_amog - 5, 180, 5, 'Amog.gif', 'Amog.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_amog.position = (0, 100, 0)

    if distance(player, Screamer_trigger_hehe) < Screamer_trigger_hehe.scale_x:
        Screamer(x_hehe + 10, y_hehe + 5, z_hehe, 90, 10, 'hehe', 'hehe.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_hehe.position = (0, 100, 0)

    if distance(player, Screamer_trigger_micro) < Screamer_trigger_micro.scale_x:
        Screamer(x_micro + 5, y_micro + 5, z_micro, 90, 10, 'micro', 'micro.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_micro.position = (0, 100, 0)


    if distance(player, enemy) < enemy.scale_x:
        Test_Screamer()
        player.position=(0, 0, 0)

        invoke(Game_over, delay=screamer_time)
        invoke(Ambient, delay=screamer_time)

    print(player.position)



    if held_keys['shift']:
        player.speed = 20
    else:
        player.speed = 10


app.run()
