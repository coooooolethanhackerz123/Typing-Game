import random
import pgzrun
from pgzhelper import *

WIDTH = 1000
HEIGHT = 800

run_imgs = ['zombie/run/tile002', 'zombie/run/tile003',
            'zombie/run/tile004', 'zombie/run/tile005']

attack_imgs = ['wizard/attack/tile000',
               'wizard/attack/tile001',
               'wizard/attack/tile002',
               'wizard/attack/tile003',
               'wizard/attack/tile004',
               'wizard/attack/tile005',
               'wizard/attack/tile006',
               'wizard/attack/tile007',]

idle_imgs = ['wizard/idle/tile000',
             'wizard/idle/tile001',
             'wizard/idle/tile002',
             'wizard/idle/tile003',
             'wizard/idle/tile004',
             'wizard/idle/tile005',]


zombie = Actor(run_imgs[0])
zombie.images = run_imgs
zombie .scale = 6
zombie.right = WIDTH
zombie.bottom = HEIGHT - 50
zombie.fps = 9

wizard = Actor(idle_imgs[0])
wizard.images = idle_imgs
wizard .scale = 2
wizard.bottom = HEIGHT + 50
wizard.fps = 9
wizard.hp = random.randint(1,5)

question = 'type to attack'
typed = ''


def update():
    zombie.animate()
    wizard.animate()
    zombie.move_towards(wizard, 1)
    if zombie.collide_pixel(wizard):
        wizard.hp -= 1
        zombie.left = WIDTH
    else:
        zombie.move_back(2)

def on_key_down(key):
    global typed
    print(key)
    if key in range (97, 122+1):
        print(chr(key))
        typed += chr(key)
    if key == 32:
        print('SPACE')
        typed +=' '
    if key == keys.BACKSPACE:
        print('DEL')
        typed = typed[0:-1]

    if typed == question:
        zombie.left = WIDTH
        typed = ''


def draw():
    screen.clear()
    screen.draw.text(f'HP:{wizard.hp}',(10,10),fontsize=50)
    screen.draw.text(question,(WIDTH/3,HEIGHT/10),fontsize=60)
    screen.draw.text(typed,(WIDTH/3,HEIGHT/10),color='orange',fontsize=60)
    zombie.draw()
    wizard.draw()
    screen.draw.text(typed,(WIDTH/3,HEIGHT/10), color='orange',fontsize=60)


pgzrun.go()
