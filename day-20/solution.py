import re
import heapq

class State:
    def __init__(self):
        self.heap = []

    def digest(self, line):
        m = re.match("^(\d+)-(\d+)$", line)
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            heapq.heappush(self.heap, (start, end))

    def process(self):
        top = 0
        while len(self.heap) > 0:
            (start, end) = heapq.heappop(self.heap)
            #print("top {}, start {}, end {}".format(top, start, end))
            if start > top:
                break
            if end > top:
                top = end + 1
        return top

def main():
    file = open("puzzle-input.txt", "r")
    state = State()
    for line in file:
        state.digest(line.strip())
    p1_result = state.process()
    print("Part 1: {} is the lowest valued IP which is not blocked".format(p1_result))

if __name__ == "__main__":
    main()
