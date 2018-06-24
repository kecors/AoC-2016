import re
from collections import deque

class State:
    def __init__(self):
        self.values = deque()
        self.bots = {}
        self.outputs = {}

    def digest(self, line):
        m = re.match("^value (\d+) goes to bot (\d+)", line)
        if m:
            self.values.append(('bot', int(m.group(2)), int(m.group(1))))
            return
        m = re.match("^bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)$", line)
        if m:
            bot = int(m.group(1))
            low_to = (m.group(2), int(m.group(3)))
            high_to = (m.group(4), int(m.group(5)))
            if bot not in self.bots:
                self.bots[bot] = { 'microchip': [] }
            self.bots[bot]['low_to'] = low_to
            self.bots[bot]['high_to'] = high_to

    def distribute(self):
        while True:
            if len(self.values) == 0:
                break

            value = self.values.popleft()
            if value[0] == 'bot':
                bot = value[1]
                microchip = value[2]
                self.bots[bot]['microchip'].append(microchip)

                if len(self.bots[bot]['microchip']) == 2:
                    min_microchip = min(self.bots[bot]['microchip'])
                    max_microchip = max(self.bots[bot]['microchip'])

                    if min_microchip == 17 and max_microchip == 61:
                        print("Part 1: bot {} is responsible for comparing value-61 microchips with value-17 microchips".format(bot))

                    low_to = self.bots[bot]['low_to']
                    self.values.append((low_to[0], low_to[1], min_microchip))

                    high_to = self.bots[bot]['high_to']
                    self.values.append((high_to[0], high_to[1], max_microchip))

                    self.bots[bot]['microchip'] = []
            else:
                output = value[1]
                microchip = value[2]
                self.outputs[output] = microchip

def main():
    state = State()
    file = open("puzzle-input.txt", "r")
    for line in file:
        state.digest(line.strip())
    state.distribute()
    product = state.outputs[0] * state.outputs[1] * state.outputs[2]
    print("Part 2: the product of the microchips in outputs 0, 1 and 2 is {}".format(product))

if __name__ == "__main__":
    main()
