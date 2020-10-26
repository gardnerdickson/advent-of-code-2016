from dataclasses import dataclass
from typing import List, Tuple
import re


@dataclass(init=False)
class SlidingWindow:
    start: int = 0
    end: int = 4

    def __init__(self, address: str, length: int = 4):
        if self.end > len(address):
            raise Exception("Address must be at least 4 characters.")
        self.address = address
        self.end = self.length = length
        self.prev_address = None
        self.in_hypernet_sequence = '[' in self.get()

    def increment(self):
        self.prev_address = self.get()
        self.start += 1
        self.end += 1
        if '[' in self.get():
            self.in_hypernet_sequence = True
        if ']' in self.prev_address and ']' not in self.get():
            self.in_hypernet_sequence = False

    def get(self):
        return self.address[self.start:self.end]

    def is_out_of_bounds(self):
        return self.end > len(self.address)

    def iter(self):
        while not self.is_out_of_bounds():
            yield self.get()
            self.increment()


def day_7_1(input_file: str) -> int:
    with open(input_file, 'r') as fh:
        addresses = fh.read().splitlines()

    tls_addresses = set()
    for address in addresses:
        window = SlidingWindow(address)
        address_invalid = False
        while not window.is_out_of_bounds() and not address_invalid:
            sub_addr = window.get()
            if sub_addr[0:2] == sub_addr[2:4][::-1] and len(set(sub_addr)) > 1:
                if window.in_hypernet_sequence:
                    address_invalid = True
                    if address in tls_addresses:
                        tls_addresses.remove(address)
                else:
                    tls_addresses.add(address)
            window.increment()
    return len(tls_addresses)


def extract_sequences(address: str) -> Tuple[List[str], List[str]]:
    supernet_regex = r'([\w]+\[|\][\w]+)'
    hypernet_regex = r'(\[[\w]+\])'
    supernet_matches = re.findall(supernet_regex, address)
    hypernet_matches = re.findall(hypernet_regex, address)
    return list(map(lambda seq: seq.strip('[').strip(']'), supernet_matches)), hypernet_matches


def find_abas(supernet_sequences: List[str]) -> List[str]:
    abas = []
    for sequence in supernet_sequences:
        window = SlidingWindow(sequence, 3)
        for substr in window.iter():
            if substr[0] == substr[2]:
                abas.append(substr)
    return abas


def find_babs(hypernet_sequences: List[str], abas: List[str]) -> bool:
    for sequence in hypernet_sequences:
        window = SlidingWindow(sequence, 3)
        for substr in window.iter():
            for aba in abas:
                bab = aba[1] + aba[0] + aba[1]
                if bab == substr:
                    return True
    return False


def day_7_2(input_file: str) -> int:
    with open(input_file, 'r') as fh:
        addresses = fh.read().splitlines()

    ssl_addresses = set()
    for address in addresses:
        supernet_sequences, hypernet_sequences = extract_sequences(address)
        abas = find_abas(supernet_sequences)
        has_bab = find_babs(hypernet_sequences, abas)
        if has_bab:
            ssl_addresses.add(address)
    return len(ssl_addresses)


answer_1 = day_7_1("input7.txt")
print(f"Part 1: {answer_1}")
answer_2 = day_7_2("input7.txt")
print(f"Part 2: {answer_2}")
