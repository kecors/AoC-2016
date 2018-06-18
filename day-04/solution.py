import re
import collections

class State:
    def __init__(self):
        self.sum = 0

    def decrypt_name(self, name, sector):
        result = ""
        for c in name:
            if c == '-':
                result += ' '
            else:
                offset = (ord(c) - ord('a') + sector) % 26
                result += chr(ord('a') + offset)
        print("{}: {}".format(sector, result))

    def evaluate(self, room):
        m = re.match("^([a-z-]+)-([0-9]+).([a-z]+).$", room)
        name = m.group(1)
        sector = int(m.group(2))
        checksum = m.group(3)

        counter = collections.Counter(name.replace("-", ""))
        counted = list(counter.most_common())
        counted.sort(key = lambda x: (-x[1], x[0]))

        top5 = ''
        for letter, _ in counted[:5]:
            top5 += letter
        if top5 == checksum:
            self.sum += sector
            self.decrypt_name(name, sector)

def main():
    state = State()
    file = open("puzzle-input.txt", "r")
    for line in file:
        state.evaluate(line.strip())
    print("Part 1: the sum of the sector IDs of the real rooms is {}".format(state.sum))

if __name__ == "__main__":
    main()
