from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
from ursina.shaders import *
from ursina.lights import PointLight
from ursina.raycaster import raycast



#light
light_position=(0,20,0)
light_position2=(0,-50,20)
Entity(model='sphere',position= light_position,scale=5,shader=lit_with_shadows_shader,color= (0,255,255, 0))
Entity(model='sphere',position= light_position2,scale=5,shader=lit_with_shadows_shader,color= (0,255,255, 0))
PointLight(position=light_position, shadows=True)
PointLight(position=light_position2, shadows=True)
shader_test = basic_lighting_shader




def map():
    level = load_model('map')
    Entity(model=level, collider=level, collision=True, scale=5, texture='grass',shader=shader_test)
    Entity(model='',  scale=10, position= (0,5,-10))

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
                         scale=5,
                         scale_x=5,
                         shader= shader_test)

    loc4_map = load_model('location_4')
    location_4 = Entity(model=loc4_map,
                        collider=loc4_map,
                        collision=True,
                        position=(0, -400, 0),
                        scale=5,
                        shader=unlit_shader)

#phone model in end
phone =Entity(model="telefon",
              texture="phone",
              rotation_y=-90,
              position=(-22.0916, -400.1, 5),
              scale=8)

visible_triggers = False

Trigger_to_loc2 = Entity(model="sphere", visible=True,color = (0,230,0,1), scale=5, position=(75, .5, 10))
Trigger_to_loc3 = Entity(model="sphere", visible=True,color = (0,230,0,1), scale=5, position=(50, -100, 10))
Trigger_EXIT = Entity(model="sphere", visible=True,color = (0,230,0,1), scale=10, position=(37.7992, -200.014, 6.35836))
Trigger_END = Entity(model="sphere", visible=visible_triggers, scale=5, position=(-22.0916, -400.207, -0.514469))



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






#enemy
class Enemy(Entity):
    def __init__(self, player, enabled=True):
        super().__init__(model="bonnie.obj", texture='texture.png', shader=shader_test, position=(-44.74, -200.182, 3.37699), collider='box')
        self.speed = 0.1
        self.player = player
        self.enabled = enabled

    def update(self):
        if not self.enabled: return
        self.look_at(self.player)
        to_player = player.position - self.position
        to_player.y = 0
        to_player.normalize()

        feet_ray = raycast(self.position + Vec3(0, 0.5, 0), to_player, ignore=(self,), distance=.5, debug=False)
        if not feet_ray.hit:
            self.position += to_player * self.speed


def Game_over():
    game_over_screen = Entity(model='quad', parent=camera.ui, scale=(2,1), texture='game over')

def END():
    ending_screen = Entity(model='quad', parent=camera.ui, scale=(2, 1), color=(0,0,0,1))
    audio.Audio(sound_file_name='Hello.mp3', loop=False)

def Test_Screamer():
    Entity(model='quad', parent=camera.ui, scale= (2,1), texture='video.mp4')
    audio.Audio(sound_file_name='sound.mp3', loop=False)


def Screamer(x,y,z, rotate, scale, screamer_vid, screamer_sound):
    screamer_back = Entity(model='quad', scale= scale, texture=screamer_vid,position=(x,y,z), rotation_y=rotate, loop=False)
    scr_audio = audio.Audio(sound_file_name=screamer_sound, loop=False)
    destroy(screamer_back,3)
    destroy(scr_audio,3)

#pause
pause_handler = Entity(ignore_paused=True)
pause_text = Text('PAUSED', origin=(0,0), scale=2, enabled=False) # Make a Text saying "PAUSED" just to make it clear when it's paused.


def pause_handler_input(key):
    if key == 'escape':
        application.paused = not application.paused     # Pause/unpause the game.
        pause_text.enabled = application.paused     # Also toggle "PAUSED" graphic.

pause_handler.input = pause_handler_input       # Assign the input function to the pause handler.



save_me = Entity(ignore_paused=True)

def save(key):
    global pp

    if key == 'left arrow':
        pp = str(player.position)

        with open('save_file.txt', 'w') as file_save:

            file_save.write(pp[5:-1])
            file_save.close()

            print('saved')

    if key == 'right arrow':
        with open('save_file.txt', 'r') as file_load:
            pp_load = file_load.read()
        print1 = pp_load.split(",") #['0','0','0']

        a = [float(i) for i in print1]
        x, y, z = a[0], a[1], a[2]
        player.position = x,y,z


    if key == 'up arrow':
        pp = (0, 0, 0)
        with open('save_file.txt', 'w') as file_delete:
            file_delete.write(str(pp)[1:-1])
            file_delete.close()
            print('save deleted')


save_me.input = save


bunny_screamer_time = 2.3
screamer_time = 3
player = FirstPersonController()
player.scale = 3
player.jump_height = 0
Sky()
map()
locations()
enemy = Enemy(player, False)

trigger_count = 0
def Triggers():
    global trigger_count
    global ringin
    if distance(player, Trigger_to_loc2) < Trigger_to_loc2.scale_x:
        player.position = (0, -99, 0)

    if distance(player, Screamer_trigger_idol) < Screamer_trigger_idol.scale_x:
        Screamer(x_idol, y_idol + 5, z_idol - 10, 180, 10, 'idol.mp4', 'idol.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_idol.position = (0, 100, 0)
        trigger_count +=1


    if distance(player, Screamer_trigger_amog) < Screamer_trigger_amog.scale_x:
        Screamer(x_amog, y_amog + 5, z_amog - 5, 180, 5, 'amog.mp4', 'Amog.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_amog.position = (0, 100, 0)
        trigger_count +=1


    if distance(player, Screamer_trigger_hehe) < Screamer_trigger_hehe.scale_x:
        Screamer(x_hehe + 10, y_hehe + 5, z_hehe, 90, 10, 'hehe', 'hehe.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_hehe.position = (0, 100, 0)
        trigger_count +=1


    if distance(player, Screamer_trigger_micro) < Screamer_trigger_micro.scale_x:
        Screamer(x_micro + 5, y_micro + 5, z_micro, 90, 10, 'micro', 'micro.mp3') # x, y, z, rotate_degree, scale, screamer_vid
        Screamer_trigger_micro.position = (0, 100, 0)
        trigger_count +=1


    if trigger_count >= 4:
        trigger_count = -1


    if trigger_count == -1:
        Trigger_to_loc3.position = (1.16471, -99, -20.3294)
        trigger_count = -2

    if trigger_count == -2:
        Trigger_to_loc2.position = (0,20000,0)



    if distance(player, Trigger_to_loc3) < Trigger_to_loc3.scale_x:
        enemy.enabled = True
        player.position = (-9.59772, -200.018, 10.3979)



    if distance(player, Trigger_EXIT) < Trigger_to_loc2.scale_x:
        player.position = (-77.7865, -400.207, -0.25065)
        ringin = audio.Audio(sound_file_name='ringing.mp3', loop=True)

    if distance(player, enemy) < enemy.scale_x:
        Test_Screamer()
        enemy.position = (0, -500, 0)
        player.position=(0, 0, 0)
        invoke(Game_over, delay=bunny_screamer_time)
        invoke(exit, delay=4)

    if distance (player, Trigger_END) < Trigger_END.scale_x:
        audio.destroy(ringin)
        END()
        player.position = (0,0,0)
        player.speed = 0
        invoke(exit, delay=3)



def update():
    enemy.update()
    Triggers()
    pause_handler_input(key='')
    save(key='')

    if distance(player, Trigger_to_loc3) < Trigger_to_loc2.scale_x:
        enemy.enabled = True
        player.position = (-9.59772, -200.018, 10.3979)
        player.rotation_y= -90




    if held_keys['shift']:
        player.speed = 13
    else:
        player.speed = 10


app.run()
