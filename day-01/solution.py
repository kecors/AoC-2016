class Position:
    orientation = 'N'
    x = 0
    y = 0
    visited = set()
    returned = False
    def turn(self, direction):
        if direction == 'L':
            if self.orientation == 'N':
                self.orientation = 'W'
            elif self.orientation == 'E':
                self.orientation = 'N'
            elif self.orientation == 'S':
                self.orientation = 'E'
            elif self.orientation == 'W':
                self.orientation = 'S'
            else:
                print("turn: invalid orientation")
        elif direction == 'R':
            if self.orientation == 'N':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'S'
            elif self.orientation == 'S':
                self.orientation = 'W'
            elif self.orientation == 'W':
                self.orientation = 'N'
            else:
                print("turn: invalid orientation")
        else:
            print("turn: invalid direction")

    def move(self, distance):
        for _ in range(distance):
            if self.orientation == 'N':
                self.y += 1
            elif self.orientation == 'E':
                self.x += 1
            elif self.orientation == 'S':
                self.y -= 1
            elif self.orientation == 'W':
                self.x -= 1
            else:
                print("move: invalid orientation");
            if self.returned == False:
                location = "{},{}".format(self.x, self.y)
                if location in self.visited:
                    self.returned = True
                    print("Part 2: return visit to {} (distance {})".format(location, self.x + self.y))
                else:
                    self.visited.add(location)

    def reveal(self):
        print("Part 1: distance = {}".format(abs(self.x) + abs(self.y)))

def run():
    with open("puzzle-input.txt", "r") as file:
        line = file.read()
        instructions = line.strip().split(", ")
        p = Position()
        for instruction in instructions:
            p.turn(instruction[0])
            p.move(int(instruction[1:]))
        p.reveal()

run()
