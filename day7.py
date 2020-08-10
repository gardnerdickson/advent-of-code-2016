from dataclasses import dataclass


@dataclass(init=False)
class SlidingWindow:
    start: int = 0
    end: int = 4

    def __init__(self, address: str):
        if self.end > len(address):
            raise Exception("Address must be at least 4 characters.")
        self.address = address
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


def day_7_1(input_file: str):
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


answer_1 = day_7_1("input7.txt")
print(f"Part 1: {answer_1}")
