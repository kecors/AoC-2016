import heapq

class State:
    FAVORITE = 1350
    WIDTH = 60
    HEIGHT = 60
    ORIGIN = (1, 1)
    TARGET = (31, 39)

    def __init__(self):
        self.grid = [False] * State.WIDTH * State.HEIGHT

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
                    output += 'B'
                    continue
                if x == State.TARGET[0] and y == State.TARGET[1]:
                    output += 'O'
                    continue
                if self.grid[y * State.WIDTH + x] == True:
                    output += 'X'
                else:
                    output += '.'
            #print output

    def distance(self, x, y):
        return abs(State.TARGET[0] - x) + abs(State.TARGET[1] - y)

    def traverse(self):
        deltas = [[0,1], [1,0], [0,-1], [-1,0]]
        heap = []
        parents = {}
        (x, y) = State.ORIGIN
        distance = self.distance(x, y)
        heapq.heappush(heap, (distance, x, y))
        while True:
            (distance, x, y) = heapq.heappop(heap)
            (target_x, target_y) = State.TARGET
            if x == target_x and y == target_y:
                path = []
                while True:
                    if (x, y) == State.ORIGIN:
                        return len(path)
                    if (x, y) in parents:
                        path.append((x, y))
                        (x, y) = parents[(x, y)]
            for (dx, dy)  in deltas:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in parents:
                    continue
                if self.grid[new_y * State.WIDTH + new_x] == False:
                    parents[(new_x, new_y)] = (x, y)
                    new_distance = self.distance(new_x, new_y)
                    heapq.heappush(heap, (new_distance, new_x, new_y))

def main():
    state = State()
    state.build_grid()
    state.display_grid()
    result = state.traverse()
    print("Part 1: the fewest number of steps required to reach (31,39) is {}".format(result))

if __name__ == "__main__":
    main()
