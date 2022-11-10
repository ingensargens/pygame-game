import simplified_pygame




class Player(simplified_pygame.EventReader):
    """ Box controlled by holding WASD on keyboard """
    def __init__(self):
        self.x = 100
        self.y = 100
        self.key_map = simplified_pygame.WASD_AS_ARROWS | simplified_pygame.DISABLE_ARROWS

    def on_hold_right(self, dur, time_passed):
        if dur > 30: self.x+=time_passed/1.5
    def on_hold_left(self, dur, time_passed):
        if dur > 30: self.x-=time_passed/1.5
    def on_hold_up(self, dur, time_passed):
        if dur > 30: self.y-=time_passed/1.5
    def on_hold_down(self, dur, time_passed):
        if dur > 30: self.y+=time_passed/1.5



