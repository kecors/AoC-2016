import collections

class State:
    def __init__(self):
        self.positions = []
        for x in range(8):
            self.positions.append([])
        self.p1_corrected_message = ''
        self.p2_corrected_message = ''

    def populate(self, message):
        for x in range(8):
            self.positions[x].append(message[x])

    def evaluate(self):
        for x in range(8):
            counter = collections.Counter(self.positions[x])
            most_common = counter.most_common()
            self.p1_corrected_message += most_common[0][0]
            self.p2_corrected_message += most_common[-1][0]

def main():
    state = State()
    file = open("puzzle-input.txt", "r")
    for line in file:
        state.populate(line.strip())
    state.evaluate()
    print("Part 1: the error-corrected version of the message is {}".format(state.p1_corrected_message))
    print("Part 2: the error-corrected version of the message is {}".format(state.p2_corrected_message))

if __name__ == "__main__":
    main()
