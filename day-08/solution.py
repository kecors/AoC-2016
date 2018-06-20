import re

MAX_X = 50
MAX_Y = 6

class State:
    def __init__(self):
        self.screen = [([False] * MAX_X) for j in range(MAX_Y)]

    def rect(self, a, b):
        for y in range(b):
            for x in range(a):
                self.screen[y][x] = True

    def rotate_row(self, a, b):
        self.screen[a] = self.screen[a][-b:] + self.screen[a][:(MAX_X - b)]

    def rotate_column(self, a, b):
        original_column = []
        for y in range(MAX_Y):
            original_column.append(self.screen[y][a])
        for y in range(MAX_Y):
            self.screen[y][a] = original_column[(MAX_Y + y - b) % MAX_Y]

    def process(self, instruction):
        match = re.match("^rect ([0-9]+)x([0-9]+)$", instruction)
        if match:
            self.rect(int(match.group(1)), int(match.group(2)))
        match = re.match("^rotate row y=([0-9]+) by ([0-9]+)$", instruction)
        if match:
            self.rotate_row(int(match.group(1)), int(match.group(2)))
        match = re.match("^rotate column x=([0-9]+) by ([0-9]+)$", instruction)
        if match:
            self.rotate_column(int(match.group(1)), int(match.group(2)))

    def lit_pixel_total(self):
        total = 0
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if self.screen[y][x] == True:
                    total += 1
        return total

    def display_screen(self):
        for y in range(MAX_Y):
            output = ""
            for x in range(MAX_X):
                if self.screen[y][x] == True:
                    output += "#"
                else:
                    output += "-"
            print output

def main():
    state = State()
    file = open("puzzle-input.txt", "r")
    for line in file:
        state.process(line.strip())
    print("Part 1: {} pixels are lit".format(state.lit_pixel_total()))

if __name__ == "__main__":
    main()
