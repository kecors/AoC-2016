#
# The strategy I used for part 2 was inspired by reading this discussion: 
#
# https://www.reddit.com/r/adventofcode/comments/5ji29h/2016_day_21_solutions/
#

import re
from itertools import permutations

class State:
    def __init__(self, password):
        self.password = password

    def swap_position(self, j, k):
        if j < k:
            a, z = j, k
        else:
            a, z = k, j
        password = self.password[:a]
        password += self.password[z]
        password += self.password[a+1:z]
        password += self.password[a]
        password += self.password[z+1:]
        self.password = password

    def rotate(self, direction, n):
        if direction == 'left':
            x = n
        else:
            x = len(self.password) - n
        self.password = self.password[x:] + self.password[:x]

    def reverse(self, j, k):
        if j < k:
            a, z = j, k
        else:
            a, z = k, j
        password = self.password[:a]
        if a == 0:
            password += self.password[z:0:-1]
            password += self.password[0]
        else:
            password += self.password[z:a-1:-1]
        password += self.password[z+1:]
        self.password = password

    def move_position(self, j, k):
        if j < k:
            password = self.password[:j]
            password += self.password[j+1:k+1]
            password += self.password[j]
            password += self.password[k+1:]
        else:
            password = self.password[:k]
            password += self.password[j]
            password += self.password[k:j]
            password += self.password[j+1:]
        self.password = password

    def digest(self, line):
        m = re.match("^swap position (\d) with position (\d)$", line)
        if m:
            j, k = int(m.group(1)), int(m.group(2))
            #print("{}: swap position {} {}".format(self.password, j, k))
            self.swap_position(j, k)
            return
        m = re.match("^swap letter ([a-z]) with letter ([a-z])$", line)
        if m:
            a, b = m.group(1), m.group(2)
            #print("{}: swap letter {} {}".format(self.password, a, b))
            self.swap_position(self.password.find(a), self.password.find(b))
            return
        m = re.match("^rotate (left|right) (\d) (steps|step)$", line)
        if m:
            direction, n = m.group(1), int(m.group(2))
            #print("{}: rotate {} {}".format(self.password, direction, n))
            self.rotate(direction, n)
            return
        m = re.match("^rotate based on position of letter ([a-z])$", line)
        if m:
            a = m.group(1)
            #print("{}: rotate by letter {}".format(self.password, a))
            j = self.password.find(a)
            if j < 4:
                self.rotate('right', j + 1)
            else:
                self.rotate('right', j + 2)
            return
        m = re.match("^reverse positions (\d) through (\d)$", line)
        if m:
            j, k = int(m.group(1)), int(m.group(2))
            #print("{}: reverse {} {}".format(self.password, j, k))
            self.reverse(j, k)
            return
        m = re.match("^move position (\d) to position (\d)$", line)
        if m:
            j, k = int(m.group(1)), int(m.group(2))
            #print("{}: move position {} {}".format(self.password, j, k))
            self.move_position(j, k)
            return

def main():
    file = open("puzzle-input.txt", "r")
    state = State("abcdefgh")
    for line in file:
        state.digest(line.strip())
    print("Part 1: The result of scrambling 'abcdefgh' is '{}'".format(state.password))

    ps = permutations("abcdefgh")
    for p in ps:
        candidate = ''.join(p)
        file = open("puzzle-input.txt", "r")
        state = State(candidate)
        for line in file:
            state.digest(line.strip())
        if "fbgdceah" == state.password:
            print("Part 2: The un-scrambled version of the scrambled password 'fbgdceah' is '{}'".format(candidate))
            break

if __name__ == "__main__":
    main()
