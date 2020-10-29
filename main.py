"""Robot module

n = number of robots
width = width of corridor
"""
import pygame as pg
import random as rnd

def dist(x, y, x1, y1):
    return ((x - x1)**2+(y - y1)**2)**0.5

class Robot:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.v = [0, 0]
        self.wait = 0
        self.current_status = -1

    def __repr__(self) -> str:
        return f"robot: x={self.x}, y={self.y}, v={self.v}, " +\
            f"wait={self.wait}, current_status={self.current_status}"

            
if __name__ == "__main__":
    n = 50
    y = 100
    width = 1350
    FPS = 60
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    robotsBuf = [Robot(35 + (i + 1) * width / (n + 2), y) for i in range(n)]
    robots = robotsBuf
    pg.init()
    SURFACE = pg.display.set_mode((1400, 500))
    '''print(*robotsBuf, sep="\n")'''
    play = True
    while play:
        SURFACE.fill((255, 255, 255))
        robotsBuf = robots
        for event in pg.event.get():
            if event.type == pg.QUIT: play = False
        # Тут нужно рандомно распределить их на группы и начать двигать 1 статус
        if robots[0].current_status == -1:
            for i in range(n):
                robotsBuf[i].current_status = rnd.randint(0, 1)
                if robotsBuf[i].current_status == 1:
                    robotsBuf[i].v = (0, 0.4)
        if robots[0].current_status > -1:
            for i in range(n):
                robotsBuf[i].y = min(robots[i].y + robots[i].v[1], \
                    130)
                robotsBuf[i].x = robots[i].x + robots[i].v[0]
            for i in range(n):
                if robots[i].current_status == 0:
                    j = 0
                    left_neibor = 0
                    left_i = i
                    right_neibor = 1350
                    right_i = i
                    for j in range(n):
                        if robots[j].current_status == 0 and i != j:
                            if left_neibor <= robots[j].x and robots[j].x < robots[i].x:
                                left_neibor = robots[j].x
                                left_i = j
                            if right_neibor >= robots[j].x and robots[j].x > robots[i].x:
                                right_neibor = robots[j].x
                                right_i = j
                    median = (right_neibor + left_neibor) / 2
                    robotsBuf[i].v = ((-robots[i].x + median) / 10, robots[i].v[1])
            for i in range(n):
                if robots[i].current_status == 1:
                    j = 0
                    left_neibor = 0
                    left_i = i
                    right_neibor = 1350
                    right_i = i
                    for j in range(n):
                        if robots[j].current_status == 1 and i != j:
                            if left_neibor <= robots[j].x and robots[j].x < robots[i].x:
                                left_neibor = robots[j].x
                                left_i = j
                            if right_neibor >= robots[j].x and robots[j].x > robots[i].x:
                                right_neibor = robots[j].x
                                right_i = j
                    median = (right_neibor + left_neibor) / 2
                    robotsBuf[i].v = ((-robots[i].x + median) / 10, robots[i].v[1])
            k = 0
            l = 0
            for i in range(n):
                if robots[i].current_status == 0:
                    k += 1
                else:
                    l += 1
            pg.display.set_caption(f"k={k}, l={l}")

        # Начать выводить крайних, подождав некоторое время

        for i in range(n):
            if robotsBuf[i].current_status:
                pg.draw.circle(SURFACE, BLUE, (int(robotsBuf[i].x), int(robotsBuf[i].y)), 2, 1)
            else:
                pg.draw.circle(SURFACE, GREEN, (int(robotsBuf[i].x), int(robotsBuf[i].y)), 2, 1)
        robots = robotsBuf
        pg.time.wait(FPS)
        pg.display.update()