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
        used = sorted(self.nodes, key=lambda n: n.used)
        avail = sorted(self.nodes, key=lambda n: n.avail, reverse=True)
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

    def display_map(self):
        xs = sorted(self.nodes, key=lambda n: n.x, reverse=True)
        x_count = xs[0].x + 1
        ys = sorted(self.nodes, key=lambda n: n.y, reverse=True)
        y_count = ys[0].y + 1
        map = ['?'] * x_count * y_count
        for node in self.nodes:
            index = node.x + (node.y * x_count)
            if node.used == 0:
                map[index] = '_'
            elif node.x == 0 and node.y == 0:
                map[index] = '0'
            elif node.x == x_count - 1 and node.y == 0:
                map[index] = 'G'
            # By observation:
            # 85 - 95 = normal size
            # 64 - 73 = normal used
            elif node.used < 85:
                map[index] = '.'
            else:
                map[index] = '#'
        for y in range(y_count):
            output = ''
            for x in range(x_count):
                output += map[x + (y * x_count)]
            print output

def main():
    file = open("puzzle-input.txt", "r")
    state = State()
    for line in file:
        state.digest(line.strip())
    print("Part 1: There are {} viable pairs of nodes".format(state.viable_pair_count()))
    # Do part 2 manually with the help of the map
    state.display_map()

if __name__ == "__main__":
    main()
