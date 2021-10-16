from ursina import *

app = Ursina()
window.fullscreen = True
Entity(model='quad', scale=7, texture="assets/message_box.png", scale_x=12)
text = Text(text="Game lost", scale=3, x=-.15, y=.35)
Text(text="You ran out of lives", scale=2, x=-.2, y=.2)
b1 = Button(text="Play again", scale_y=.1, x=-.3, y=-.1, scale_x=.3, color=color.green)
Button(text="Exit", scale_y=.1, x=.3, y=-.1, scale_x=.3, color=color.red)

app.run()
