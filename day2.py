from lib import Point

increments = {
    'U': Point(-1, 0),
    'D': Point(1, 0),
    'L': Point(0, -1),
    'R': Point(0, 1)
}


def day_2_1(input_file):
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    with open(input_file) as file:
        lines = file.readlines()
    current_position = Point(2, 2)
    code = []
    for line in lines:
        for instruction in line.replace('\n', ''):
            current_position = current_position.add(increments[instruction]).clamp(0, 0, len(keypad[0]) - 1,
                                                                                   len(keypad) - 1)
        code.append(str(keypad[current_position.x][current_position.y]))
    return "".join(code)


def day_2_2(input_file):
    keypad = [['_', '_', '1', '_', '_'],
              ['_', '2', '3', '4', '_'],
              ['5', '6', '7', '8', '9'],
              ['_', 'A', 'B', 'C', '_'],
              ['_', '_', 'D', '_', '_']]
    with open(input_file) as file:
        lines = file.readlines()
    current_position = Point(2, 0)
    code = []
    for line in lines:
        for instruction in line.replace('\n', ''):
            last_position = current_position
            current_position = current_position.add(increments[instruction]).clamp(0, 0, len(keypad[0]) - 1,
                                                                                   len(keypad) - 1)
            if keypad[current_position.x][current_position.y] == '_':
                current_position = last_position
        code.append(str(keypad[current_position.x][current_position.y]))
    return "".join(code)


answer_1 = day_2_1("input2.txt")
print("Part 1: " + str(answer_1))
answer_2 = day_2_2("input2.txt")
print("Part 2: " + str(answer_2))
