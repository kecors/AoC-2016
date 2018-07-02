#
# I got some inspiration for part 2 from the following discussion, 
# and in particular the comment by adventofcode2016:
#
# https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/dbdg0oh/
#

class Elf:
    def __init__(self, id):
        self.id = id
        self.left = id + 1
        self.right = id - 1
        self.presents = 1

    def display(self):
        print("{}: left {}, right {}, presents {}".format(self.id, self.left, self.right, self.presents))

def process_p1(elf_count):
    elves = {}
    for j in range(elf_count):
        elf = j + 1
        elves[elf] = Elf(elf)
    elves[elf_count].left = 1
    elves[1].right = elf_count

    elf = 1
    while True:
        left_elf = elves[elf].left
        elves[elf].presents += elves[left_elf].presents
        elves[elf].left = elves[left_elf].left
        if elves[elf].left == elf:
            return elf
        else:
            elf = elves[elf].left

def display_elves(elves):
    for elf in elves:
        elves[elf].display()

def process_p2(elf_count):
    elves = {}
    for j in range(elf_count):
        elf = j + 1
        elves[elf] = Elf(elf)
    elves[elf_count].left = 1
    elves[1].right = elf_count

    thief = 1
    target = thief + (elf_count / 2)
    while True:
        #display_elves(elves)
        #print("{}: Now {} steals from {}".format(elf_count, thief, target))
        elves[thief].presents += elves[target].presents

        left = elves[target].left
        right = elves[target].right
        elves[left].right = right
        elves[right].left = left

        elves[target].left = target
        elves[target].right = target
        elves[target].presents = 0

        elf_count -= 1
        if elf_count % 2 == 1:
            target = left
        else:
            target = elves[left].left

        if elves[thief].left == thief:
            return thief
        else:
            thief = elves[thief].left


def main():
    elf_count = int(open("puzzle-input.txt", "r").read().strip())
    p1_result = process_p1(elf_count)
    print("Part 1: elf {} gets all the presents".format(p1_result))
    p2_result = process_p2(elf_count)
    print("Part 2: elf {} gets all the presents".format(p2_result))

if __name__ == "__main__":
    main()
