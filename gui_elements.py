import pygame as pg


class OriginButton:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
    
    def is_over(self):
        x, y = pg.mouse.get_pos()
        return self.rect.collidepoint(x, y)


color_edge = [(255, 0, 0), (0, 255, 0)]
color_background = (100, 100, 100)
color_text = (255, 255, 255)
width_edge = 3


class TextButton(OriginButton):
    pg.init()
    font = pg.font.SysFont('songti', 18)

    def __init__(self, x, y, w, h, text):
        super().__init__(x, y, w, h)
        self.text = text
        self.text_surface = font.render(self.text, False, color_text)
        self.text_x = self.x + (self.w - self.text_surface.get_width()) // 2
        self.text_y = self.y + (self.h - self.text_surface.get_height()) // 2
    
    def draw(self, surface):
        if self.is_over():
            pg.draw.rect(surface, color_edge[1], self.rect)
        else:
            pg.draw.rect(surface, color_edge[0], self.rect)
        pg.draw.rect(surface, color_background, pg.Rect(self.x+width_edge, self.y+width_edge, self.w-width_edge*2, self.h-width_edge*2))
        surface.blit(self.text_surface, (self.text_x, self.text_y))


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((400,400))
    clock = pg.time.Clock()
    font = pg.font.SysFont('SimHei',24)
    start_button = TextButton(150, 150, 60, 30, text='开始')
    quit_button = TextButton(150, 190, 60, 30, text='退出')
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        clock.tick(120)
        screen.fill((0,0,0))
        start_button.draw(screen)
        quit_button.draw(screen)
        screen.blit(font.render(str(int(clock.get_fps())), True, (255,0,0)),(10,10))
        pg.display.update()
