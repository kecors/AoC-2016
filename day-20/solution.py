import re
import heapq

class State:
    def __init__(self):
        self.heap_p1 = []
        self.heap_p2 = []

    def digest(self, line):
        m = re.match("^(\d+)-(\d+)$", line)
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            heapq.heappush(self.heap_p1, (start, end))
            heapq.heappush(self.heap_p2, (start, end))

    def process_p1(self):
        top = 0
        while len(self.heap_p1) > 0:
            (start, end) = heapq.heappop(self.heap_p1)
            #print("top {}, start {}, end {}".format(top, start, end))
            if start > top:
                break
            if end > top:
                top = end + 1
        return top

    def process_p2(self):
        total = 0
        top = 0
        while len(self.heap_p2) > 0:
            (start, end) = heapq.heappop(self.heap_p2)
            #print("total {}, top {}, start {}, end {}".format(total, top, start, end))
            if start > top:
                total += start - top
                top = start
            if end > top:
                top = end + 1
        return total

def main():
    file = open("puzzle-input.txt", "r")
    state = State()
    for line in file:
        state.digest(line.strip())
    p1_result = state.process_p1()
    print("Part 1: {} is the lowest valued IP which is not blocked".format(p1_result))
    p2_result = state.process_p2()
    print("Part 2: {} IPs are allowed by the blacklist".format(p2_result))

if __name__ == "__main__":
    main()
