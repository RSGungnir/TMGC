import pyagme as 
import sys
from collections import defaultdict
import numpy as np

from gui import GUI
import config as c

class Tamagochi:
    def __init__(self):
        self.is_running = True
        self.dt = 0
        self.screen = pg.display.set_mode((c.SCR_W, c.SCR_H))
        self.clock = pg.time.Clock()
        self.gui = GUI()
        self.key_handlers = defaultdict(list)
    
    def reset_data(self):
        pass
    
    def show_fps(self):
        pg.display.set_caption('FPS: ' + str(int(self.clock.get_fps()/2)))
    
    def handler(self, e_type, key):
        if e_type == pg.KEYDOWN:
            if key == pg.K_p:
                self.run_pause_menu()
            elif key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
    
    def setup_key_handlers(self):
        pass
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def run_save_slot_menu(self):
        pass
    
    def run_game(self):
        while self.is_running:
            self.handle_events()
            self.clock.tick()
            self.update()
            self.draw()
            pg.display.update()
            self.dt = self.clock.tick()
            self.show_fps()
    
    def run(self):
        self.run_save_slot_menu()
        
        while True:
            self.run_game()
    