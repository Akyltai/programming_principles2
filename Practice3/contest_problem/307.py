import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance
x1, y1 = map(int, input().split())
p1 = Point(x1, y1)
p1.show()

move_x, move_y = map(int, input().split())
p1.move(move_x, move_y)
p1.show()


x2, y2 = map(int, input().split())
p2 = Point(x2, y2)

distance = p1.dist(p2)
print(f"{distance:.2f}")