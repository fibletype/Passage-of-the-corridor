# n = number of robots
# width = width of corridor

n = 150
x = 100
width = 1000

robots = []
 

class robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 0
        self.wait = 0
        self.currentStatus = -1

def summonRobots(n, width, robots):
    for i in range(n):
        robots.append(robot(x, i * width / (n + 2)))
    return robots


robotsBuf = summonRobots(n, width, robots)
print(robotsBuf)