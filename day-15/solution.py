import re

class Disc:
    def __init__(self, level, positions, start):
        self.level = level
        self.positions = positions
        self.start = start

    def slot_aligned(self, time):
        if 0 == (time + self.level + self.start) % self.positions:
            return True
        else:
            return False

class State:
    def __init__(self):
        self.discs = []

    def digest(self, line):
        m = re.match("^Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+).", line)
        if m:
            level = int(m.group(1))
            positions = int(m.group(2))
            start = int(m.group(3))
            disc = Disc(level, positions, start)
            self.discs.append(disc)
            return

    def add_part2_disc(self):
        disc = Disc(7, 11, 0)
        self.discs.append(disc)

    def process(self):
        time = 0
        while True:
            if all([disc.slot_aligned(time) for disc in self.discs]):
                return time
            time += 1

def main():
    file = open("puzzle-input.txt", "r")
    state = State()
    for line in file:
        state.digest(line.strip())
    p1_result = state.process()
    print("Part 1: {} is the first time you can get a capsule".format(p1_result))
    file = open("puzzle-input.txt", "r")
    state = State()
    for line in file:
        state.digest(line.strip())
    state.add_part2_disc()
    p2_result = state.process()
    print("Part 2: {} is the first time you can get a capsule".format(p2_result))

if __name__ == "__main__":
    main()
