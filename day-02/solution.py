ADJACENTS_P1 = { '1': { 'U': '1', 'R': '2', 'D': '4', 'L': '1' },
                 '2': { 'U': '2', 'R': '3', 'D': '5', 'L': '1' },
                 '3': { 'U': '3', 'R': '3', 'D': '6', 'L': '2' },
                 '4': { 'U': '1', 'R': '5', 'D': '7', 'L': '4' },
                 '5': { 'U': '2', 'R': '6', 'D': '8', 'L': '4' },
                 '6': { 'U': '3', 'R': '6', 'D': '9', 'L': '5' },
                 '7': { 'U': '4', 'R': '8', 'D': '7', 'L': '7' },
                 '8': { 'U': '5', 'R': '9', 'D': '8', 'L': '7' },
                 '9': { 'U': '6', 'R': '9', 'D': '9', 'L': '8' }
               }
ADJACENTS_P2 = { '1': { 'U': '1', 'R': '1', 'D': '3', 'L': '1' },
                 '2': { 'U': '2', 'R': '3', 'D': '6', 'L': '2' },
                 '3': { 'U': '1', 'R': '4', 'D': '7', 'L': '2' },
                 '4': { 'U': '4', 'R': '4', 'D': '8', 'L': '3' },
                 '5': { 'U': '5', 'R': '6', 'D': '5', 'L': '5' },
                 '6': { 'U': '2', 'R': '7', 'D': 'A', 'L': '5' },
                 '7': { 'U': '3', 'R': '8', 'D': 'B', 'L': '6' },
                 '8': { 'U': '4', 'R': '9', 'D': 'C', 'L': '7' },
                 '9': { 'U': '9', 'R': '9', 'D': '9', 'L': '8' },
                 'A': { 'U': '6', 'R': 'B', 'D': 'A', 'L': 'A' },
                 'B': { 'U': '7', 'R': 'C', 'D': 'D', 'L': 'A' },
                 'C': { 'U': '8', 'R': 'C', 'D': 'C', 'L': 'B' },
                 'D': { 'U': 'B', 'R': 'D', 'D': 'D', 'L': 'D' }
               }

class State:
    def __init__(self, adjacents):
        self.adjacents = adjacents
        self.position = '5'
        self.solution = ""

    def process(self, instructions):
        self.position = '5'
        for instruction in instructions:
            self.position = self.adjacents[self.position][instruction]
        self.solution += self.position

def main():
    with open("puzzle-input.txt", "r") as file:
        state_p1 = State(ADJACENTS_P1)
        state_p2 = State(ADJACENTS_P2)
        for line in file:
            state_p1.process(line.strip())
            state_p2.process(line.strip())
        print("Part 1: the bathroom code is {}".format(state_p1.solution))
        print("Part 2: the bathroom code is {}".format(state_p2.solution))

if __name__ == "__main__":
    main()
