import re
from functools import reduce


def day_3_1(input_file):
    with open(input_file) as file:
        lines = file.readlines()
    valid_count = 0
    for line in lines:
        a, b, c = parse_line(line)
        if is_triangle(a, b, c):
            valid_count += 1
    return valid_count


def day_3_2(input_file):
    with open(input_file) as file:
        flattened = flatten_input(file.readlines())
    valid_count = 0
    sides = side_generator(flattened)
    for a, b, c in sides:
        if is_triangle(a, b, c):
            valid_count += 1
    return valid_count


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def flatten_input(lines):
    a_col = []
    b_col = []
    c_col = []
    for line in lines:
        a, b, c = parse_line(line)
        a_col.append(a)
        b_col.append(b)
        c_col.append(c)
    flatten = [a_col, b_col, c_col]
    return reduce(lambda x, y: x + y, flatten)


def side_generator(side_list):
    for i in range(0, len(side_list), 3):
        yield side_list[i], side_list[i + 1], side_list[i + 2]


def parse_line(line):
    group = re.search("(\s)*(?P<a>\d*)(\s)*(?P<b>\d*)(\s)*(?P<c>\d*)", line)
    return int(group['a']), int(group['b']), int(group['c'])


answer_1 = day_3_1("input3.txt")
print("Part 1: " + str(answer_1))
answer_2 = day_3_2("input3.txt")
print("Part 2: " + str(answer_2))
