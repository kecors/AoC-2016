class State:
    adjacents = { 1: { 'U': 1, 'R': 2, 'D': 4, 'L': 1 },
                  2: { 'U': 2, 'R': 3, 'D': 5, 'L': 1 },
                  3: { 'U': 3, 'R': 3, 'D': 6, 'L': 2 },
                  4: { 'U': 1, 'R': 5, 'D': 7, 'L': 4 },
                  5: { 'U': 2, 'R': 6, 'D': 8, 'L': 4 },
                  6: { 'U': 3, 'R': 6, 'D': 9, 'L': 5 },
                  7: { 'U': 4, 'R': 8, 'D': 7, 'L': 7 },
                  8: { 'U': 5, 'R': 9, 'D': 8, 'L': 7 },
                  9: { 'U': 6, 'R': 9, 'D': 9, 'L': 8 }
                }
    position = 5
    solution = ""
    def process(self, instructions):
        self.postion = 5
        for instruction in instructions:
            self.position = self.adjacents[self.position][instruction]
        self.solution += `self.position`

def main():
    with open("puzzle-input.txt", "r") as file:
        state = State()
        for line in file:
            state.process(line.strip())
        print("Part 1: the bathroom code is {}".format(state.solution))

if __name__ == "__main__":
    main()
