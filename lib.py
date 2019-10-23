from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)

    def move(self, x, y):
        return Point(self.x + x, self.y + y)
