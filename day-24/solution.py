import heapq
from itertools import permutations

class State:
    DELTAS = [[0,1], [1,0], [0,-1], [-1,0]]

    def __init__(self, lines):
        self.pois = [None] * 8
        self.grid = []
        self.routes = {}
        self.shortest_path = (9999, None)

        y = 0
        for line in lines:
            x = 0
            for c in line:
                digit = "01234567".find(c)
                if digit is not -1:
                    self.pois[int(digit)] = (x, y)
                if c == '#':
                    self.grid.append(True)
                else:
                    self.grid.append(False)
                x += 1
            self.max_x = x
            y += 1
        self.max_y = y

    def find_shortest_route(self, pois_start, pois_end):
        (start_x, start_y) = self.pois[pois_start]
        (end_x, end_y) = self.pois[pois_end]
        heap = []
        dte = abs(end_x - start_x) + abs(end_y - start_y)
        heapq.heappush(heap, (dte, start_x, start_y))
        parent = {}
        parent[(start_x, start_y)] = (start_x, start_y, 0)
        while True:
            if len(heap) == 0:
                break
            (dte, x, y) = heapq.heappop(heap)
            if (x, y) == (end_x, end_y):
                (px, py, pt) = parent[(x, y)]
                steps = []
                steps.append((x, y))
                while pt > 0:
                    steps.append((px, py))
                    (px, py, pt) = parent[(px, py)]
                if (pois_start, pois_end) in self.routes:
                    current_len = len(self.routes[(pois_start, pois_end)])
                    if len(steps) >= current_len:
                        continue
                self.routes[(pois_start, pois_end)] = steps[::-1]
            for (dx, dy) in State.DELTAS:
                new_x, new_y = x + dx, y + dy
                if self.grid[new_y * self.max_x + new_x] == True:
                    continue
                (px, py, pt) = parent[(x, y)]
                if (new_x, new_y) in parent:
                    (nx, ny, nt) = parent[(new_x, new_y)]
                    if (pt + 1) >= nt:
                        continue
                parent[(new_x, new_y)] = (x, y, pt + 1)
                dte = abs(end_x - new_x) + abs(end_y - new_y)
                heapq.heappush(heap, (dte, new_x, new_y))

    def calculate_minimum_steps(self):
        for j in range(8):
            for k in range(j + 1, 8):
                self.find_shortest_route(j, k)
        for p in permutations(range(8)):
            sum = 0
            for x in range(7):
                start_poi = min(p[x], p[x+1])
                end_poi = max(p[x], p[x+1])
                sum += len(self.routes[start_poi, end_poi]) - 1
            if sum < self.shortest_path[0]:
                self.shortest_path = (sum, p)

def main():
    file = open("puzzle-input.txt", "r")
    contents = file.read()
    state = State(contents.strip().split("\n"))
    state.calculate_minimum_steps()
    print("Part 1: the fewest number of steps is {}".format(state.shortest_path[0]))

if __name__ == "__main__":
    main()
