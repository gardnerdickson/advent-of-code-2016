from enum import Enum, auto
from lib import Point


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

class Position:

    class DirectionInfo:
        def __init__(self, next_left, next_right, x_multiplier, y_multiplier):
            self.next_left = next_left
            self.next_right = next_right
            self.x_multiplier = x_multiplier
            self.y_multiplier = y_multiplier

    direction_info_table = {
        Direction.NORTH: DirectionInfo(Direction.WEST, Direction.EAST, 0, 1),
        Direction.EAST: DirectionInfo(Direction.NORTH, Direction.SOUTH, 1, 0),
        Direction.SOUTH: DirectionInfo(Direction.EAST, Direction.WEST, 0, -1),
        Direction.WEST: DirectionInfo(Direction.SOUTH, Direction.NORTH, -1, 0)
    }

    def __init__(self, location, direction):
        self.location = location
        self.direction = direction

    def __str__(self):
        return "location: {0}, direction: {1}".format(self.location, self.direction)

    def move(self, turn, amount):
        if turn == 'L':
            direction = Position.direction_info_table[self.direction].next_left
        else:
            direction = Position.direction_info_table[self.direction].next_right
        location = self.location.move(
            amount * Position.direction_info_table[direction].x_multiplier,
            amount * Position.direction_info_table[direction].y_multiplier
        )
        return Position(location, direction)

    def range(self, position):
        if self.location.x == position.location.x:
            step = 1 if self.location.y < position.location.y else -1
            points = map(lambda y: Point(self.location.x, y), range(self.location.y + (1 * step), position.location.y + (1 * step), step))
        elif self.location.y == position.location.y:
            step = 1 if self.location.x < position.location.x else -1
            points = map(lambda x: Point(x, self.location.y), range(self.location.x + (1 * step), position.location.x + (1 * step), step))
        else:
            raise RuntimeError("Positions are not aligned")
        return list(points)


def day_1_1(input_file):
    file = open(input_file, "r")
    instructions = file.read().split(", ")
    file.close()
    current_position = Position(Point(0, 0), Direction.NORTH)
    for (turn, amount) in parse(instructions):
        current_position = current_position.move(turn, amount)
    return abs(current_position.location.x) + abs(current_position.location.y)


def day_1_2(input_file):
    file = open(input_file, "r")
    instructions = file.read().split(", ")
    file.close()
    current_position = Position(Point(0, 0), Direction.NORTH)
    visited = set()
    for (turn, amount) in parse(instructions):
        new_position = current_position.move(turn, amount)
        locations = current_position.range(new_position)
        for location in locations:
            if location in visited:
                return abs(location.x) + abs(location.y)
            visited.add(location)
        current_position = new_position
    return None

def parse(instructions):
    return map(lambda instruction: (instruction[:1], int(instruction[1:])), instructions)


answer_1 = day_1_1("input1.txt")
print("Part 1: " + str(answer_1))
answer_2 = day_1_2("input1.txt")
print("Part 2: " + str(answer_2))
