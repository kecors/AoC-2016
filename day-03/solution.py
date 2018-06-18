def main():
    total = 0
    columns = [ [], [], [] ] # For part 2
    file = open("puzzle-input.txt", "r")
    for line in file:
        sides = " ".join(line.split()).split(' ')
        sides = list(map(lambda x: int(x), sides))
        for j in range(3):
            columns[j].append(sides[j])
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            total += 1
    print("Part 1: {} of the listed triangles are possible".format(total))

    total = 0
    for j in range(3):
        while len(columns[j]) > 0:
            sides = []
            for _ in range(3):
                sides.append(columns[j].pop())
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                total += 1
    print("Part 2: {} of the listed triangles are possible".format(total))

if __name__ == "__main__":
    main()
