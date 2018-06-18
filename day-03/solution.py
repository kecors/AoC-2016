def main():
    with open("puzzle-input.txt", "r") as file:
        total = 0
        for line in file:
            sides = " ".join(line.split()).split(' ')
            sides = list(map(lambda x: int(x), sides))
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                total += 1
        print("Part 1: {} of the listed triangles are possible".format(total))

if __name__ == "__main__":
    main()
