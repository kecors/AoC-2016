import re

class Node:
    def __init__(self, x, y, size, used, avail, use_percentage):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.use_percentage = use_percentage

    def display(self):
        print("{}-{} {} : {} / {}".format(self.x, self.y, self.size, self.used, self.avail))

class State:
    def __init__(self):
        self.nodes = []

    def digest(self, line):
        m = re.match("^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$", line)
        if m:
            x = int(m.group(1))
            y = int(m.group(2))
            size = int(m.group(3))
            used = int(m.group(4))
            avail = int(m.group(5))
            use_percentage = int(m.group(6))
            node = Node(x, y, size, used, avail, use_percentage)
            self.nodes.append(node)

    def viable_pair_count(self):
        used = sorted(self.nodes, key=lambda x: x.used)
        avail = sorted(self.nodes, key=lambda x: x.avail, reverse=True)
        all_pairs = 0
        for u_node in used:
            if u_node.used == 0:
                continue
            pairs = 0
            for a_node in avail:
                if u_node.x == a_node.x and u_node.y == a_node.y:
                    continue
                if u_node.used <= a_node.avail:
                    pairs += 1
                else:
                    break
            all_pairs += pairs
        return all_pairs

def main():
    file = open("puzzle-input.txt", "r")
    state = State()
    for line in file:
        state.digest(line.strip())
    print("Part 1: There are {} viable pairs of nodes".format(state.viable_pair_count()))

if __name__ == "__main__":
    main()
