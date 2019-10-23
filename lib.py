from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)

    def move(self, x, y):
        return Point(self.x + x, self.y + y)

    def clamp(self, x_min, y_min, x_max, y_max):
        x = max(x_min, min(self.x, x_max))
        y = max(y_min, min(self.y, y_max))
        return Point(x, y)

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def copy(self):
        return Point(self.x, self.y)
