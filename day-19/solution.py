class Elf:
    def __init__(self, id):
        self.id = id
        self.left = id + 1
        self.presents = 1

def process(elf_count):
    elves = {}
    for j in range(elf_count):
        elf = j + 1
        elves[elf] = Elf(elf)
    elves[elf_count].left = 1

    elf = 1
    while True:
        left_elf = elves[elf].left
        elves[elf].presents += elves[left_elf].presents
        elves[elf].left = elves[left_elf].left
        if elves[elf].left == elf:
            return elf
        else:
            elf = elves[elf].left

def main():
    elf_count = int(open("puzzle-input.txt", "r").read().strip())
    p1_result = process(elf_count)
    print("Part 1: elf {} gets all the presents".format(p1_result))

if __name__ == "__main__":
    main()
