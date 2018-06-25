class State:
    FAVORITE = 1350

    def __init__(self):
        self.width = 32
        self.height = 40
        self.grid = [False] * self.width * self.height

    def determine(self, x, y):
        result = x*x + 3*x + 2*x*y + y + y*y + State.FAVORITE
        binary = bin(result)
        if binary.count('1') % 2 == 1:
            return True
        else:
            return False

    def build_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y * self.width + x] = self.determine(x, y)

    def display_grid(self):
        for y in range(self.height):
            output = ""
            for x in range(self.width):
                if x == 1 and y == 1:
                    output += 'B'
                    continue
                if x == 31 and y == 39:
                    output += 'O'
                    continue
                if self.grid[y * self.width + x] == True:
                    output += 'X'
                else:
                    output += '.'
            print output

def main():
    state = State()
    state.build_grid()
    state.display_grid()

if __name__ == "__main__":
    main()
