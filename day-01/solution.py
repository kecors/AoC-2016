class State:
    (x, y) = (0, 0) # Origin
    deltas = [ (0, 1), (1, 0), (0, -1), (-1, 0) ] # N, E, S, W
    direction = 0 # Index into deltas, default to N
    turns = { 'L': -1, 'R': 1 } # Affects direction
    visited = set()
    awaitingRevisit = True

    def move(self, turn, distance):
        self.direction = (self.direction + self.turns[turn]) % 4
        delta = self.deltas[self.direction]
        for _ in range(distance):
            self.x += delta[0]
            self.y += delta[1]
            if self.awaitingRevisit == True:
                location = "{},{}".format(self.x, self.y)
                if location in self.visited:
                    print("Part 2: The first location visited twice is {} blocks away ({})".format((self.x + self.y), location))
                    self.awaitingRevisit = False
                else:
                    self.visited.add(location)

def main():
    with open("puzzle-input.txt", "r") as file:
        line = file.read()
        instructions = line.strip().split(", ")
        state = State()
        for instruction in instructions:
            state.move(instruction[0], int(instruction[1:]))
        print("Part 1: Easter Bunny HQ is {} blocks away".format(abs(state.x) + abs(state.y)))

if __name__ == "__main__":
    main()
