from enum import Enum, auto

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

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        return "x: {0}, y: {1}, direction: {2}".format(self.x, self.y, self.direction)

    def move(self, turn, amount):
        if turn == 'L':
            self.direction = Position.direction_info_table[self.direction].next_left
        else:
            self.direction = Position.direction_info_table[self.direction].next_right
        self.x += amount * Position.direction_info_table[self.direction].x_multiplier
        self.y += amount * Position.direction_info_table[self.direction].y_multiplier


def day_1(input_file):
    file = open(input_file, "r")
    instructions = file.read().split(", ")
    file.close()
    current_position = Position(0, 0, Direction.NORTH)
    for (turn, amount) in parse(instructions):
        current_position.move(turn, amount)
    print(abs(current_position.x) + abs(current_position.y))


def parse(instructions):
    return map(lambda instruction: (instruction[:1], int(instruction[1:])), instructions)


day_1("input1.txt")
