"""Robot module

n = number of robots
width = width of corridor
"""
import pygame as pg

FPS = 60

class Robot:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.v = 0
        self.wait = 0
        self.current_status = -1

    def __repr__(self) -> str:
        return f"robot: x={self.x}, y={self.y}, v={self.v}, " +\
            f"wait={self.wait}, current_status={self.current_status}"

            
if __name__ == "__main__":
    n = 100
    y = 100
    width = 1350
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    robotsBuf = [Robot(35 + int((i) * width / (n + 2)), y) for i in range(n)]
    pg.init()
    SURFACE = pg.display.set_mode((1400, 500))
    '''print(*robotsBuf, sep="\n")'''
    play = True
    while play:
        SURFACE.fill((255, 255, 255))
        for event in pg.event.get():
            if event.type == pg.QUIT: play = False
        

        pg.display.set_caption("Test drawing")
        for i in range(n):
            pg.draw.circle(SURFACE, BLUE, (robotsBuf[i].x, robotsBuf[i].y), 2, 1)
        pg.time.wait(FPS)
        pg.display.update()