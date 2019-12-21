import re
from dataclasses import dataclass, replace

from lib import get_lines, cat


@dataclass
class RoomInfo:
    name: str
    sector_id: int
    checksum: str


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def day_4_1(room_names: list) -> int:
    rooms = map(parse_room_name, room_names)
    valid_rooms = filter(lambda room: room.checksum == generate_checksum(room.name), rooms)
    sector_id_sum = sum(map(lambda room: room.sector_id, valid_rooms))
    return sector_id_sum


def day_4_2(room_names: list, print_filter: str) -> None:
    rooms = map(parse_room_name, room_names)
    valid_rooms = filter(lambda room: room.checksum == generate_checksum(room.name), rooms)
    for decrypted_room in map(lambda room: decrypt_room_name(room), valid_rooms):
        if print_filter in decrypted_room.name:
            print(f"Decrypted room name: {decrypted_room.name}, Sector Id: {decrypted_room.sector_id}")


def decrypt_room_name(room: RoomInfo) -> RoomInfo:
    decrypted_room_name = list()
    for character in room.name:
        if character == '-':
            decrypted_room_name.append(" ")
        else:
            index = alphabet.index(character)
            rotated_index = (index + room.sector_id) % len(alphabet)
            decrypted_room_name.append(alphabet[rotated_index])
    return replace(room, name="".join(decrypted_room_name))


def generate_checksum(encrypted_name: str) -> str:
    char_count = {}
    for c in encrypted_name.replace("-", ""):
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    alphabetically_sorted = sorted(char_count.items())
    count_sorted = {k: v for k, v in sorted(alphabetically_sorted, key=lambda item: item[1], reverse=True)}
    return cat(list(count_sorted.keys())[:5])


def parse_room_name(room_name: str) -> RoomInfo:
    groups = re.search("(?P<room>([a-zA-Z]+(-))+)(?P<sector>[\d]+)(?P<checksum>(\[)[\w]+(\]))", room_name)
    return RoomInfo(groups['room'][:-1], int(groups['sector']), groups['checksum'].replace('[', '').replace(']', ''))


input_lines = get_lines("input4.txt")
answer_1 = day_4_1(input_lines)
print(f"Part 1: {answer_1}")
answer_2 = day_4_2(input_lines, "north")
print(f"Part 2: {answer_2}")
