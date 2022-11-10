
from simplified_pygame import *
from player import *
from application import *
WINDOW = PyGameWindow(640, 480)

app = Application(w=WINDOW)
box = Player()

for events, time_passed, key_pressed in WINDOW.main_loop(framerate=60):
    box.read_events(events, time_passed, key_pressed)
    app.read_events(events, time_passed, key_pressed)
    WINDOW.rect((box.x, box.y+100, 10, 10), col=(52, 209, 244))
# rgba(52,209,244,255)