import re

from lib import get_lines


def day_8():
    screen = [['.' for _ in range(50)] for _ in range(6)]

    rect_cmd_regex = r'rect (?P<rows>[0-9]+)x(?P<cols>[0-9]+)'
    rotate_cmd_regex = r'rotate (?P<dimension>[\w]+) (x|y)=(?P<index>[0-9]+) by (?P<amount>[0-9]+)'

    for command in get_lines('input8.txt'):
        rect_match = re.match(rect_cmd_regex, command)
        if rect_match:
            rect(screen, int(rect_match.group('rows')), int(rect_match.group('cols')))
        rotate_match = re.match(rotate_cmd_regex, command)
        if rotate_match:
            rotate(screen, rotate_match.group('dimension'), int(rotate_match.group('index')), int(rotate_match.group('amount')))

    lights = 0
    for row in screen:
        for cell in row:
            lights += 1 if cell == '#' else 0

    return lights


def rect(screen, width, height):
    for y in range(height):
        for x in range(width):
            screen[y][x] = '#'


def rotate(screen, dimension, index, amount):
    data_indices = []
    if dimension == 'row':
        for col in range(len(screen[index])):
            if screen[index][col] == '#':
                data_indices.append(col)
        data_indices = set([(x + amount) % len(screen[index]) for x in data_indices])
        for col, data in enumerate(screen[index]):
            if col in data_indices:
                screen[index][col] = '#'
            else:
                screen[index][col] = '.'
    else:
        data_indices = []
        for row in range(len(screen)):
            if screen[row][index] == '#':
                data_indices.append(row)
        data_indices = [(x + amount) % len(screen) for x in data_indices]
        for row, data in enumerate(screen):
            if row in data_indices:
                screen[row][index] = '#'
            else:
                screen[row][index] = '.'


answer_1 = day_8()
print(f"Part 1: {answer_1}")
