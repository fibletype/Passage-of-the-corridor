"""Robot module

n = number of robots
width = width of corridor
"""
import pygame as pg
import random as rnd
import math

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
    n = 20
    y = 100
    a = 0
    width = 1350
    FPS = 10
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    robotsBuf = [Robot(35 + (i + 1) * width / (n + 2), y) for i in range(n)]
    robots = robotsBuf
    pg.init()
    SURFACE = pg.display.set_mode((1400, 500))
    '''print(*robotsBuf, sep="\n")'''
    for i in range(n):
        robotsBuf[i].current_status = rnd.randint(0, 1)
        if robotsBuf[i].current_status == 1:
            robotsBuf[i].v = (0, 0.4)
    average_velocity = 0
    play = True
    while play:
        SURFACE.fill((255, 255, 255))
        robotsBuf = robots
        for event in pg.event.get():
            if event.type == pg.QUIT:
                play = False

            # Пересчет скоростей

            for i in range(n):
                robotsBuf[i].y = max(100, min(robots[i].y + robots[i].v[1], \
                    130))
                robotsBuf[i].x = robots[i].x + robots[i].v[0]

            # Плотность верхних

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

            # Плотность нижних

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

            # Подсчет количества роботов в ряду

            k = 0
            l = 0
            for i in range(n):
                if robots[i].current_status == 0:
                    k += 1
                else:
                    l += 1
                average_velocity += math.fabs(robots[i].v[0])
            average_velocity /= n
            pg.display.set_caption(f"k={k}, l={l}")


        # Формирования равенства в рядах

        if average_velocity <= 0.01 and a == 0:
            a = 2000
            left_up = -1
            left_down = -1
            for i in range(n):
                if left_down == -1:
                    if robots[i].current_status == 1:
                        left_down = i
                elif robots[i].x < robots[left_down].x and robots[i].current_status == 1:
                    left_down = i
                if left_up == -1:
                    if robots[i].current_status == 0:
                        left_up = i
                elif robots[i].x < robots[left_up].x and robots[i].current_status == 0:
                    left_up = i
            if math.fabs(robots[left_up].x - robots[left_down].x) > 0.07:
                if robots[left_up].x < robots[left_down].x:
                    robots[left_up].current_status = 1
                    robots[left_up].v = (0, 0.1)
                if robots[left_up].x > robots[left_down].x:
                    robots[left_down].current_status = 0
                    robots[left_down].v = (0, -0.1)
            pg.display.set_caption(f"down={robots[left_down].current_status} up={left_up}")
            pg.time.wait(3000)
        elif a > 0:
            a -= 1

        # отрисовка

        for i in range(n):
            if robotsBuf[i].current_status:
                pg.draw.circle(SURFACE, BLUE, (int(robotsBuf[i].x), int(robotsBuf[i].y)), 2, 1)
            else:
                pg.draw.circle(SURFACE, GREEN, (int(robotsBuf[i].x), int(robotsBuf[i].y)), 2, 1)
        robots = robotsBuf
        pg.time.wait(FPS)
        pg.display.update()
