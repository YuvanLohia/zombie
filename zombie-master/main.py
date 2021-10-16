from os import cpu_count
from random import randint, uniform
from ursina import *
import webbrowser,json

class Zombie1(Entity):
    def __init__(self):
        pos = (uniform(-6, 6), -8.9, 69)
        super().__init__(
            model="quad",
            texture='assets/zombies/zombie1.png',

            position=pos,
            scale_y=3.5,
            scale_x=2,
            collider='box'

        )
        self.model = "quad"
        self.position = pos
        self.scale_y = 3.5
        self.scale_x = 2
        self.texture = 'assets/zombies/zombie1.png'
        self.lives = 1
        self.collider = 'box'

    def hit(self):
        global zombies

        self.lives -= 1.3
        if self.lives < 0:
            self.dead()

    def dead(self):
        global zombies, score
        yes.start()
        destroy(self)
        zombies.remove(self)
        score += 1
        score_display.text = f"Score :{score}"

    def cross(self):
        global zombies, score

        destroy(self)
        zombies.remove(self)
        score += 1
        score_display.text = f"Score :{score}"


class Zombie2(Entity):
    def __init__(self):
        pos = (uniform(-6, 6), -8.9, 69)
        super().__init__(
            model="quad",
            texture='assets/zombies/zombie2.png',

            position=pos,
            scale=3.5,
            collider='box'

        )
        self.model = "quad"
        self.position = pos
        self.scale = 3.5
        self.texture = 'assets/zombies/zombie2.png'
        self.lives = 2
        self.collider = 'box'

    def hit(self):
        global zombies

        self.lives -= 1.3
        if self.lives < 0:
            self.dead()

    def dead(self):
        global zombies, score
        yes.start()
        destroy(self)
        zombies.remove(self)
        score += 1
        score_display.text = f"Score :{score}"

    def cross(self):
        global zombies, score

        destroy(self)
        zombies.remove(self)
        score += 1
        score_display.text = f"Score :{score}"


class Zombie3(Entity):
    def __init__(self):
        pos = (uniform(-6, 6), -8.9, 69)
        super().__init__(
            model="quad",
            texture='assets/zombies/zombie3.png',

            position=pos,
            scale=3,
            collider='box'

        )
        self.model = "quad"
        self.position = pos
        self.scale = 3
        self.texture = 'assets/zombies/zombie3.png'
        self.lives = 3
        self.collider = 'box'

    def hit(self):
        global zombies

        self.lives -= 1.3
        if self.lives < 0:
            self.dead()

    def dead(self):
        global zombies, score
        yes.start()
        destroy(self)
        zombies.remove(self)
        score += 1
        score_display.text = f"Score :{score}"

    def cross(self):
        global zombies, score

        destroy(self)
        zombies.remove(self)
        score += 1
        score_display.text = f"Score :{score}"


def bullet():
    gullet = Entity(model='assets/gun/bullet.obj', color=color.rgb(175, 155, 96),
                    position=(camera.x + .5, camera.y + 1.2, -3), scale=.1, collider='box', rotation_x=180)
    return gullet


# variable
entity_list = []
once = False


def play_again():
    os.execl(sys.executable, sys.executable, *sys.argv)


def close_play():
    global current_type, message_show
    for jk in entity_list:
        destroy(jk)
    gun.show()
    for i in lives_list:
        i.show()
    main_screen.hide()
    score_display.show()
    bullets_display.show()
    bullet_display.show()
    message_show = False


def back():
    global current_type
    current_type = "init"


def how_to():
    webbrowser.open(r"C:\Users\BBL\Documents\.python\zombie-master\how_to_play.html")
def shopper():
    global current_type,once
    for jk in entity_list:
        destroy(jk)
    once =  False
    current_type = "shop"
def choose_gun(gunss):
    global jdic,current_gun,no_bullets
    if current_gun != gunss:
        jdic["guns"] = gunss
        current_gun = gunss
        if gunss == "gun2":
            no_bullets = jdic["bullets"]
        else:
            no_bullets = 900
        bullets_display.text=f"Bullets :{no_bullets}"   
        gun.texture = guns[current_gun][0]
        gun.scale = guns[current_gun][1]
    
        with open("data.json","w") as f:
            json.dump(jdic,f)
def by():
    global jdic,once,coins
    if coins >= 2000:
        for jk in entity_list:
            destroy(jk)
        coins -= 2000
        jdic["coins"] = coins
        jdic["gun2"] = True
        jdic["bullets"] = 1200
        with open("data.json","w") as f:
            json.dump(jdic,f)
        once =  False
def update():
    global blood_screen,once, main_screen, zombies, lives_gun, speed, difficulty, score, lives_gone_indicator, message_show, current_type, entity_list,coins,jdic
    if not message_show:
        if not held_keys['shift']:
            if camera.x < 6:
                camera.x += held_keys['right arrow'] * time.dt * 5
            if camera.x > -6:
                camera.x -= held_keys['left arrow'] * time.dt * 5
            if camera.y < 5:
                camera.y += held_keys['up arrow'] * time.dt * 5
            if camera.x > -5:
                camera.y -= held_keys['down arrow'] * time.dt * 5

        for k in zombies:
            try:
                k.z -= .02 * speed
            except:
                pass
            if k.z < 0:
                lives_gone_indicator.start()
                lives_list[int(lives_gun - 1 // 1)].texture = 'assets/lives/empty.png'
                lives_gun -= 1
                blood_screen.color = color.rgba(255,0,0,(3-lives_gun)*30)
                k.cross()

        if len(zombies) < difficulty:
            if difficulty < 5.9:
                zv = Zombie1()
                zombies.append(zv)
            elif 13.9 > difficulty > 5.9:
                no = randint(1, 2)
                if no == 1:
                    zv = Zombie1()
                    zombies.append(zv)
                else:
                    zv = Zombie2()
                    zombies.append(zv)
            elif score < 450:
                no = randint(1, 3)
                if no == 1:
                    zv = Zombie1()
                    zombies.append(zv)
                elif no == 2:
                    zv = Zombie2()
                    zombies.append(zv)
                else:
                    zv = Zombie3()
                    zombies.append(zv)
            else:
                message_show = True
                current_type = "won"
        if len(bullets) > 0:
            for bullet_obj in bullets:
                try:
                    bullet_obj.z += .8
                    bullet_obj.y += .003
                    hit_info = bullet_obj.intersects()
                    if hit_info.hit:
                        hit_info.entity.hit()
                        destroy(bullet_obj)
                        bullets.remove(bullet_obj)

                except:
                    pass

        if lives_gun == 0:
            message_show = True
            current_type = "lost"
            blood_screen.color = color.rgba(0,0,0,200)
        if once:
            once = False
        speed += 0.0035
        difficulty += 0.002
    elif not once:

        gun.hide()
        for i in lives_list:
            i.hide()

        score_display.hide()
        bullets_display.hide()
        bullet_display.hide()

        main_screen.show()
        if current_type == "won":
            t1 = Text(text="Game Won", scale=5, x=-.33, y=.45)
            entity_list.append(t1)
            t2 = Text(text="You killed 450 zombies. You get 1000 coins", scale=3, x=-.8, y=.18)
            entity_list.append(t2)
            coins += 1000
            jdic["coins"] = coins
            if current_gun == "gun2":
                if no_bullets == 0:
                    jdic["gun2"] = False
                    choose_gun("gun1")
                    t5 = Text(text="You have finished all your bullets kindly purchase them from the shop",x = -.5)
                    entity_list.append(t5)
                else:
                    t5 = Text(text="You have used {} bullets. You have {} bullets remaining.".format(jdic["bullets"] - no_bullets,no_bullets),x = -.5)
                    entity_list.append(t5)
                    
                    jdic['bullets'] -= jdic["bullets"] - no_bullets
                    
            with open("data.json","w") as f:
                json.dump(jdic,f)
            b1 = Button(icon = "assets/buttons/play.png" ,x=-.1, y=-.15, color=color.green,scale = .1)
            b1.tooltip = Tooltip("Play Again")
            entity_list.append(b1)
            b2 = Button(x=.1, y=-.15,icon = "assets/buttons/exit.png", color=color.red,scale = .1)
            b2.tooltip = Tooltip("Exit")
            entity_list.append(b2)
            b2.on_click = app.destroy
            b1.on_click = play_again
        elif current_type == "lost":
            coins += 50 * (score // 50)
            jdic["coins"] = coins
            if current_gun == "gun2":
                if no_bullets == 0:
                    jdic["gun2"] = False
                    choose_gun("gun1")
                    t5 = Text(text="You have finished all your bullets kindly purchase them from the shop",x = -.5)
                    entity_list.append(t5)
                else:
                    t5 = Text(text="You have used {} bullets. You have {} bullets remaining.".format(jdic["bullets"] - no_bullets,no_bullets),x = -.5)
                    entity_list.append(t5)
                    jdic['bullets'] -= jdic["bullets"] - no_bullets
                    
                
            with open("data.json","w") as f:
                json.dump(jdic,f)
            t1 = Text(text="Game Lost", scale=5, x=-.33, y=.45)
            entity_list.append(t1)
            t2 = Text(text="You ran out of lives. You get {} coins.".format(50 * (score // 50)), scale=3, x=-.7, y=.18)
            entity_list.append(t2)
            b1 = Button(icon = "assets/buttons/play.png" ,x=-.1, y=-.15, color=color.green,scale = 0.1)
            b1.tooltip = Tooltip("Play Again")
            entity_list.append(b1)
            b2 = Button(x=.1, y=-.15,icon = "assets/buttons/exit.png", color=color.red,scale = .1)
            b2.tooltip = Tooltip("Exit")
            entity_list.append(b2)
            b2.on_click = app.destroy
            b1.on_click = play_again
        elif current_type == "init":
            e1 = Entity(model="quad", texture="assets/text/Zombie.png", position=(0, -4.85, 0), scale=.7, scale_y=.5)
            entity_list.append(e1)
            e2 = Entity(model="quad", texture="assets/text/hole.png", position=(0, -5, -.1), scale=.3)
            entity_list.append(e2)
            e3 = Entity(model="quad", texture="assets/text/Shooutout.png", position=(.1, -5.1, 0), scale=.2, scale_x=.5)
            entity_list.append(e3)
            e4 = Entity(model="quad", texture="assets/zombies/zombie3.png", position=(.5, -5.25, 0), scale=.4)
            entity_list.append(e4)
            e5 = Entity(model="quad", texture="assets/zombies/zombie1.png", position=(-.5, -4.9, 0), scale=.3,
                        scale_y=.5)
            entity_list.append(e5)
            e6 = Entity(model="quad", texture="assets/zombies/zombie2.png", position=(.55, -4.75, 0), scale=.4)
            entity_list.append(e6)
            b1 = Button(x=-.3 , y=-.4, color=color.rgb(128, 255, 0), scale=.1, icon="assets/buttons/play.png")
            entity_list.append(b1)
            b1.tooltip = Tooltip("Play")
            b1.on_click = close_play
            b4 = Button(x=-.15, y=-.4, color=color.rgb(255, 255, 26), scale=.1, icon="assets/buttons/back.png")
            entity_list.append(b4)
            b4.tooltip = Tooltip("Shop")
            b4.on_click = shopper
            b2 = Button(x=-0, y=-.4, color=color.rgb(50, 50, 255), scale=.1, icon="assets/buttons/how.png")
            entity_list.append(b2)
            b2.tooltip = Tooltip("How to play")
            b2.on_click = how_to
            b3 = Button(x=.2, y=-.4, color=color.rgb(255, 0, 0), scale=.1, icon="assets/buttons/exit.png")
            entity_list.append(b3)
            b3.tooltip = Tooltip("exit")
            b3.on_click = app.destroy

        elif current_type == "shop":
            coin = Entity(model = "quad",texture = "assets\coin.png",scale = .1,position = (.5,-4.7,0))
            entity_list.append(coin)
            t2 = Text(text = str(coins),scale = 2,x = .7,y = .39)
            entity_list.append(t2)
            t1 = Text(text="Shop", scale=5, x=-.1, y=.45)
            entity_list.append(t1)  
            e1 = Entity(model = "quad",texture = "assets/gun/1.png",scale = .2,scale_x = .5,position=(-.4, -4.85, 0))
            entity_list.append(e1)
            e2 = Entity(model = "quad",texture = "assets/gun/2.png",scale = .2,scale_x = .5,position=(-.4, -5.1, 0))
            entity_list.append(e2)
            t2 = Text(text = "Bullets = 900 \n Cost : Free",scale = 1.5,y = .25)
            entity_list.append(t2)
            t3 = Text(text = "Bullets = 1200 \n Cost : 2000",scale = 1.5,y = -.1)
            entity_list.append(t3)
            b3 = Button(text  = "Choose",color = color.green,x = .5,y =.2,scale = .1,scale_x = .2)
            b3.on_click = lambda : choose_gun("gun1")
            entity_list.append(b3)
            if jdic["gun2"]:
                b4 = Button(text  = "Choose",color = color.green,x = .5,y =-.15,scale = .1,scale_x = .2)
                b4.on_click = lambda : choose_gun("gun2")
            else:
                b4 = Button(text  = "Buy",color = color.rgb(255, 195, 77),x = .5,y =-.15,scale = .1,scale_x = .2)
                b4.on_click = by
            entity_list.append(b4)
            b1 = Button(icon = "assets/buttons/play.png" ,x=-.1, y=-.35, color=color.green,scale = 0.1)
            b1.tooltip = Tooltip("Play")
            entity_list.append(b1)
            b2 = Button(x=.1, y=-.35,icon = "assets/buttons/exit.png", color=color.red,scale = .1)
            b2.tooltip = Tooltip("Exit")
            entity_list.append(b2)
            b2.on_click = app.destroy
            b1.on_click = close_play
        if jdic['bullets'] == 0:
            jdic["gun2"] = False
            with open("data.json","w") as f:
                json.dump(jdic,f)
        once = True


def input(key):
    global zombies, difficulty, no_bullets, bullets

    if key == 'space' and no_bullets > 0:
        no_bullets -= 1
        bullets_display.text = f"Bullets :{no_bullets}"
        Audio('assets/gun/fire.wav')
        b = bullet()
        bullets.append(b)
        Audio('assets/gun/reload.wav')


jdic = {"coins":0,"guns":"gun1","bullets":0,"gun2":False}
try:
    with open("data.json","x") as f:
        json.dump(jdic,f)
except:
    with open("data.json","r") as f:
        jdic = json.load(f)
coins = jdic["coins"]
app = Ursina()
main_screen = Entity(model='quad', color=color.rgba(0, 0, 0, 200),
                     position=(0, -5, 0), scale=3)
main_screen.hide()
blood_screen = Entity(model = "quad",color = color.rgba(255,0,0,0),scale = 20,parent = camera.ui)
zombies = []
lives_gun = 3
score = 0

live1quad = Entity(model='quad', texture='assets/lives/full.png', scale=.1, position=(-.8, .4, 0), parent=camera.ui)
live2quad = Entity(model='quad', texture='assets/lives/full.png', scale=.1, position=(-.69, .4, 0),
                   parent=camera.ui)
live3quad = Entity(model='quad', texture='assets/lives/full.png', scale=.1, position=(-.58, .4, 0),
                   parent=camera.ui)
lives_list = [live1quad, live2quad, live3quad]
score_display = Text(text=f"Score :{score}", position=(.7, .45, 0), parent=camera.ui)

bullet_display = Entity(model="quad", texture="assets/gun/bullet.png", position=(.63, .4, 0), parent=camera.ui,
                        scale_y=.1, scale_x=.07)
yes = Animation("assets/plus/", fps=3, position=(0, 0.25, 0), parent=camera.ui, loop=False, scale=.2, scale_y=0.1)

lives_gone_indicator = Animation("assets/minus/", fps=3, position=(0, 0.25, 0), parent=camera.ui, loop=False,
                                 scale=.2,
                                 scale_y=0.1)
difficulty = 0
speed = 1
bullets = []

guns = {"gun1": ["assets/gun/gun1.png",1.2,900], "gun2": ["assets/gun/gun2.png",1.6,1200]}
current_gun = jdic["guns"]
if current_gun == "gun2":
    no_bullets = jdic["bullets"]
else:
    no_bullets = 900
bullets_display = Text(text=f"Bullets :{no_bullets}", position=(.70, .4, 0), parent=camera.ui)
background_main = Entity(model='quad', texture='assets/background.jpg', position=(0, 0, 70), scale=120.1)
gun = Entity(model='quad', parent=camera.ui, texture= guns[current_gun][0], position=(0, 0, 0), scale=guns[current_gun][1])
message = False
# after

camera.y -= 5
camera.z = 0
message_show = True

current_type = "init"
for i in range(difficulty):
    v = Zombie1()
    zombies.append(v)

camera.z = - 2
print(camera.y)
app.run()
