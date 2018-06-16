class Position:
    orientation = 'N'
    x = 0
    y = 0
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
        if self.orientation == 'N':
            self.y += distance
        elif self.orientation == 'E':
            self.x += distance
        elif self.orientation == 'S':
            self.y -= distance
        elif self.orientation == 'W':
            self.x -= distance
        else:
            print("move: invalid orientation");

    def reveal(self):
        print("distance = {}".format(self.x + self.y))

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
