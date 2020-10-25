"""Robot module

n = number of robots
width = width of corridor
"""

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
    n = 150
    x = 100
    width = 1000
    robotsBuf = [Robot(x, i * width / (n + 2)) for i in range(n)]
    print(*robotsBuf, sep="\n")
