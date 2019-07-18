import pygame as pg

from TMGC import Tamagochi


def main():
    pg.mixer.pre_init(44100, 16, 4, 1024)
    pg.init()
    
    Tamagochi().run()


if __name__ == '__main__':
    main()
