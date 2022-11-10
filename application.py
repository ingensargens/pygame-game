import simplified_pygame
import pygame
class Application(simplified_pygame.EventReaderAsClass):
    WINDOW = None
    def __init__(self, w:simplified_pygame.PyGameWindow):
        global WINDOW
        super().__init__()
        WINDOW = w
    def on_key_f1():
        global WINDOW
        WINDOW.set_window_resolution(1)
    def on_key_f11():
        global WINDOW
        WINDOW.set_window_resolution('fullscreen')
    def on_key_escape():
        global WINDOW
        WINDOW.exit()
