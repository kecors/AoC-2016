import re
import collections

class State:
    def __init__(self):
        self.sum = 0

    def evaluate(self, room):
        room = room.replace("-", "")
        m = re.match("^([a-z]+)([0-9]+).([a-z]+).$", room)
        name = m.group(1)
        sector = int(m.group(2))
        checksum = m.group(3)

        counter = collections.Counter(name)
        counted = list(counter.most_common())
        counted.sort(key = lambda x: (-x[1], x[0]))

        top5 = ''
        for letter, _ in counted[:5]:
            top5 += letter
        if top5 == checksum:
            self.sum += sector

def main():
    state = State()
    file = open("puzzle-input.txt", "r")
    for line in file:
        state.evaluate(line.strip())
    print("Part 1: the sum of the sector IDs of the real rooms is {}".format(state.sum))

if __name__ == "__main__":
    main()
