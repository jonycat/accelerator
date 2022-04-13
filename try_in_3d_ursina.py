from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
from ursina.shaders import *
from ursina.lights import PointLight

#light

light_position=(0,20,0)
light_position2=(0,-50,20)
Entity(model='sphere',position= light_position,scale=5,shader=lit_with_shadows_shader,color= (0,255,255, 1))
Entity(model='sphere',position= light_position2,scale=5,shader=lit_with_shadows_shader,color= (0,255,255, 1))
PointLight(position=light_position, shadows=True)
PointLight(position=light_position2, shadows=True)
shader_test = basic_lighting_shader




def map():
    level = load_model('map')
    Entity(model=level, collider=level, collision=True, scale=5, texture='grass',shader=shader_test)



def locations(): #Create environment
    home_outside = Entity(model="home_outside_model",
                      collider="home_outside_model",
                      collision=True,
                      texture='house_outside_texture',
                      position=(100,0,0),scale=1,
                      rotation_y=180,shader=shader_test)


    home_inside = Entity(model="house_inside",
                     collider="house_inside",
                     collision=True,
                     texture='brick',
                     position=(0,-100,-30),
                     scale=33,
                     rotation_y=180,shader=shader_test)


    home_inside_roof = Entity(model='plane',
                              texture='grass',
                              position=(0,-89,0),scale=90,
                              rotation_x=180)

    #-44.74, -192.182, 3.37699
    location_3  = Entity(model="location_3",
                         collider="location_3",
                         collision=True,
                         texture="location_3",
                         position=(0,-200,0),
                         scale=4,
                         scale_x=5,
                         shader= shader_test)




#temporary_enemy
enemy = Entity(model="bonnie.obj",texture='texture.png', position=(1,.5,3),shader=shader_test)

#temporary_Triggers
visible_triggers = True

Trigger_1 = Entity(model="sphere",visible=visible_triggers, scale=10,position=(75,.5,10))
Trigger_Guys = Entity(model="sphere",visible=visible_triggers,scale=10,position=(50,.5,10))
Trigger_loc3 = Entity(model="sphere",visible=visible_triggers,scale=10,position=(37.7992, -200.014, 9.35836))

#Trigger_Screamer
#settings
x = 30
y = 0
z = 0
scale_z = 5

x_idol, y_idol, z_idol = -27.1282, -98.7348, -8.82384
x_amog, y_amog, z_amog = 29.0178, -98.02, 11.3805
x_hehe, y_hehe, z_hehe = 12.0208, -98.02, -12.9324
x_micro, y_micro, z_micro = 11.4192, -98.02, 10.8022


Screamer_trigger_idol = Entity(model="sphere",visible=visible_triggers,position=(x_idol, y_idol, z_idol),shader=triplanar_shader,scale=5)
Screamer_trigger_amog = Entity(model="sphere",visible=visible_triggers,position=(x_amog, y_amog, z_amog),shader=triplanar_shader,scale=5)
Screamer_trigger_hehe = Entity(model="sphere",visible=visible_triggers,position=(x_hehe, y_hehe, z_hehe),shader=triplanar_shader,scale=5)
Screamer_trigger_micro = Entity(model="sphere",visible=visible_triggers,position=(x_micro, y_micro, z_micro),shader=triplanar_shader,scale=5)




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
    scr = Entity(model='quad', scale= (scale), texture=screamer_vid,position=(x,y,z), rotation_y=rotate, loop=False)
    a = audio.Audio(sound_file_name=screamer_sound, loop=False)
    destroy(scr,3)
    destroy(a,3)



bunny_screamer_time = 2.3
screamer_time = 3
player = FirstPersonController()

player.scale = 3
player.jump_height = 20
Sky()
map()
locations()

def amog_coords():
    x_amog, y_amog, z_amog = -40.885, 0, -0.295287


def update():
    if distance(player, Trigger_1) < Trigger_1.scale_x:
        player.position = (0, -99, 0)

    if distance(player,Trigger_Guys) < Trigger_1.scale_x:
        player.position = (-44.74, -200.182, 3.37699)

    if distance(player,Trigger_loc3) < Trigger_1.scale_x:
        player.position = (0,0,0)

    if distance(player, Screamer_trigger_idol) < Screamer_trigger_idol.scale_x:
        Screamer(x_idol, y_idol + 5, z_idol - 10, 180, 10, 'idol.mp4', 'idol.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_idol.position = (0, 100, 0)


    if distance(player, Screamer_trigger_amog) < Screamer_trigger_amog.scale_x:
        Screamer(x_amog, y_amog + 5, z_amog - 5, 180, 5, 'amog.mp4', 'Amog.mp3') # x, y, z, rotate_degree, scale, screamer_vid
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

        invoke(Game_over, delay=bunny_screamer_time)
        invoke(Ambient, delay=bunny_screamer_time)

    print(player.position)



    if held_keys['shift']:
        player.speed = 20
    else:
        player.speed = 10


app.run()
