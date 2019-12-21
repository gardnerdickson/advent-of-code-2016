
from hashlib import md5
from typing import Tuple, Optional

from lib import cat


def day_5_1(door_id: str) -> str:
    door_id += '#'
    index = 0
    password = ""
    while len(password) != 8:
        hasher = md5()
        hash_input = door_id.replace("#", str(index))
        hasher.update(hash_input.encode('utf-8'))
        door_hash = hasher.hexdigest()
        if door_hash.startswith('00000'):
            print(f"Hash: {door_hash}")
            password += door_hash[5]
        index += 1
    return password


def day_5_2(door_id: str) -> str:

    def check_hash(door_hash: str) -> Optional[Tuple[int, str]]:
        if door_hash.startswith('00000') and door_hash[5].isnumeric() and int(door_hash[5]) < 8:
            return int(door_hash[5]), door_hash[6]
        else:
            return None

    door_id += "#"
    index = 0
    password = ['_', '_', '_', '_', '_', '_', '_', '_']
    while '_' in password:
        hasher = md5()
        hash_input = door_id.replace("#", str(index))
        hasher.update(hash_input.encode('utf-8'))
        door_hash = hasher.hexdigest()
        p_val = check_hash(door_hash)
        if p_val is not None and password[p_val[0]] == '_':
            password[p_val[0]] = p_val[1]
            print(f"Password: {cat(password)}")
        index += 1
    return cat(password)


puzzle_input = 'ugkcyxxp'
answer_1 = day_5_1(puzzle_input)
print(f"Part 1: {answer_1}")
answer_2 = day_5_2(puzzle_input)
print(f"Part 2: {answer_2}")
