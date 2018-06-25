class State:
    FAVORITE = 1350
    WIDTH = 60
    HEIGHT = 60
    ORIGIN = (1, 1)
    TARGET = (31, 39)
    DELTAS = [[0,1], [1,0], [0,-1], [-1,0]]

    def __init__(self):
        self.grid = [False] * State.WIDTH * State.HEIGHT
        self.parent = {}

    def is_wall(self, x, y):
        result = x*x + 3*x + 2*x*y + y + y*y + State.FAVORITE
        binary = bin(result)
        if binary.count('1') % 2 == 1:
            return True
        else:
            return False

    def build_grid(self):
        for y in range(State.HEIGHT):
            for x in range(State.WIDTH):
                self.grid[y * State.WIDTH + x] = self.is_wall(x, y)

    def display_grid(self):
        for y in range(State.HEIGHT):
            output = ""
            for x in range(State.WIDTH):
                if x == State.ORIGIN[0] and y == State.ORIGIN[1]:
                    output += 'O'
                    continue
                if x == State.TARGET[0] and y == State.TARGET[1]:
                    output += 'T'
                    continue
                if self.grid[y * State.WIDTH + x] == True:
                    output += '#'
                else:
                    output += '.'
            print output

    def distance_to_origin(self, x, y):
        sum = 0
        while (x, y) != State.ORIGIN:
            (x, y) = self.parent[(x, y)]
            sum += 1
        return sum

    def traverse(self):
        self.parent[State.ORIGIN] = State.ORIGIN
        stack = [State.ORIGIN]
        while True:
            if len(stack) == 0:
                break
            (x, y) = stack.pop()
            dist = self.distance_to_origin(x, y)
            for (dx, dy) in State.DELTAS:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0:
                    continue
                if self.grid[new_y * State.WIDTH + new_x] == True:
                    continue
                if (new_x, new_y) in self.parent:
                    (px, py) = self.parent[(new_x, new_y)]
                    if dist < self.distance_to_origin(px, py):
                        self.parent[(new_x, new_y)] = (x, y)
                        stack.append((new_x, new_y))
                else:
                    self.parent[(new_x, new_y)] = (x, y)
                    stack.append((new_x, new_y))

    def at_most_50_steps(self):
        sum = 0
        for (x, y) in self.parent:
            if self.distance_to_origin(x, y) <= 50:
                sum += 1
        return sum

def main():
    state = State()
    state.build_grid()
    #state.display_grid()
    state.traverse()
    (tx, ty) = state.TARGET
    p1_result = state.distance_to_origin(tx, ty)
    p2_result = state.at_most_50_steps()
    print("Part 1: the fewest number of steps required to reach (31,39) is {}".format(p1_result))
    print("Part 2: {} locations can be reached in at most 50 steps".format(p2_result))

if __name__ == "__main__":
    main()
