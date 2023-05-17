from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

score=0
ammo=12

def pozitie():
    global a, b, c
    a=random.randint(-45, 45)
    b=1.1
    c=random.randint(-45, 45)

def culoare():
    global R, G, B
    R=random.randint(0, 255)
    G=random.randint(0, 255)
    B=random.randint(0, 255)

app=Ursina()

Sky()

for z in range(3):
    for x in range(3):
        Entity(model="cube", scale=(100, 1, 100), texture="podea.png", parent=scene, collider="box", ignore=False)
perete1=Entity(model="cube", scale=(100, 10, 1), position=(0, 5.5, 50), collider="box", texture="perete.png")
perete2=Entity(model="cube", scale=(100, 10, 1), position=(0, 5.5, -50), collider="box", texture="perete.png")
perete3=Entity(model="cube", scale=(100, 10, 1), position=(50, 5.5, 0), collider="box", texture="perete.png")
perete3.rotation_y=90
perete4=Entity(model="cube", scale=(100, 10, 1), position=(-50, 5.5, 0), collider="box", texture="perete.png")
perete4.rotation_y=90

player=FirstPersonController(model="om.glb", scale=(2, 2.5, 2))
camera.z=-1
camera.y=-1
camera.x=0.3

bullet=None

pause=Text(text="Pause (press 'o' to resume)", x=-0.4, y=0.3, scale=3, visible=False)

def input(key):
    global bullet, ammo, score
    if ammo>0:
        if key == 'left mouse down':
            ammo-=1
            bullet = Entity(parent=player, model='cube', scale=(0.1, 0.1, 0.1), color=color.black, collider='box')
            bullet.world_parent = scene
            bullet.animate_position(bullet.position+(bullet.forward*2000), curve=curve.linear, duration=3)
            destroy(bullet, delay=3)
    if key == 'b up':
        score-=3
        ammo+=12
    if key=='p up':
        player.enabled=False
        pause.visible=True
    if key=='o up':
        player.enabled=True
        pause.visible=False

cube=None
cube2=None

def cub1():
    global cube
    pozitie()
    culoare()
    cube=Entity(model="cube", scale=(1, 1, 1), collider="box", position=(a, b, c), color=rgb(R, G, B))
def cub2():
    global cube2
    pozitie()
    culoare()
    cube2=Entity(model="cube", scale=(1, 1, 1), collider="box", position=(a, b, c), color=rgb(R, G, B))

warn=Text(text="Buy Ammo NOW! (press 'b' to buy)", x=-0.6, y=0, scale=3, visible=False)

cub1()
cub2()

texte=Text(text=("Score: " + str(score)), x=-0.73, y=-0.45)
magazie=Text(text=("Ammo: " + str(ammo)), x=0.57, y=-0.45)

def update():
    global cube, cube2, bullet, score, ammo, warn

    texte.text=("Score: " + str(score))
    magazie.text=("Ammo: " + str(ammo))

    if bullet and bullet.intersects(cube).hit:
        hit_info = bullet.intersects(cube)
        destroy(bullet)
        destroy(cube)
        cub1()
        if distance(player, cube)>40:
            score+=2
        else:
            score+=1

    if bullet and bullet.intersects(cube2).hit:
        hit_info = bullet.intersects(cube2)
        destroy(bullet)
        destroy(cube2)
        cub2()
        if distance(player, cube2)>40:
            score+=3
        else:
            score+=2

    if bullet and bullet.intersects(perete1).hit:
        score-=1
    if bullet and bullet.intersects(perete2).hit:
        score-=1
    if bullet and bullet.intersects(perete3).hit:
        score-=1
    if bullet and bullet.intersects(perete4).hit:
        score-=1
    if ammo<=0:
        warn.visible=True
    else:
        warn.visible=False
    
app.run() 