
from lib import get_lines

from typing import Callable


def day_6(messages: list, priority_func: Callable) -> str:
    error_corrected = ""
    for i in range(0, 8):
        char_counts = count_chars(messages, i)
        error_corrected += priority_func(char_counts, key=char_counts.get)
    return error_corrected


def count_chars(messages: list, index: int) -> dict:
    char_count = {}
    for message in messages:
        char = message[index]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


lines = get_lines("input6.txt")
answer_1 = day_6(lines, max)
print(f"Part 1: {answer_1}")
answer_2 = day_6(lines, min)
print(f"Part 2: {answer_2}")
