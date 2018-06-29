class State:
    def __init__(self, row):
        self.rows = [row]
        self.triggers = ['^^.', '.^^', '^..', '..^']

    def process(self):
        j = 1 # row number
        while j < 40:
            above_row = '.' + self.rows[j-1] + '.'
            new_row = '.'
            k = 0 # column number
            while k < len(above_row) - 1:
                if above_row[k:k+3] in self.triggers:
                    new_row += '^'
                else:
                    new_row += '.'
                k += 1
            self.rows.append(new_row[1:-1])
            j += 1

    def count_safe_tiles(self):
        sum = 0
        for row in self.rows:
            sum += row.count('.')
        return sum

def main():
    row1 = open("puzzle-input.txt", "r").read().strip()
    state = State(row1)
    state.process()
    p1_result = state.count_safe_tiles()
    print("Part 1: there are {} safe tiles".format(p1_result))

if __name__ == "__main__":
    main()
