#
# NOTE: I got some good ideas from reading the following:
#
# https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/
#
# - re.search() is more appropriate than re.match() for this problem
# - For the provided input, it is safe to assume that the scope of
#   a child repetition never exceeds the scope of its parent
#   repetition
# - Recursion is one good approach to part 2 of this problem
#

import re

def p1_decompress(data):
    index = 0
    length = 0
    while True:
        match = re.search("\((\d+)x(\d+)\)", data[index:])
        if match:
            offset, a, b = match.start(), match.group(1), match.group(2)
            length += offset + int(a) * int(b)
            index += offset + len(a) + len(b) + 3 + int(a)
        else:
            length += len(data) - index
            break
    return length

def p2_decompress(data):
    index = 0
    length = 0
    while True:
        match = re.search("\((\d+)x(\d+)\)", data[index:])
        if match:
            offset, a, b = match.start(), match.group(1), match.group(2)
            token_length = len(a) + len(b) + 3
            sub_offset = index + offset + token_length
            sub_length = p2_decompress(data[sub_offset:sub_offset+int(a)])
            length += offset + sub_length * int(b)
            index += offset + token_length + int(a)
        else:
            length += len(data) - index
            break
    return length

def main():
    data = open("puzzle-input.txt", "r").read().strip()
    length = p1_decompress(data)
    print("Part 1: the decompressed length of the file is {}".format(length))
    length = p2_decompress(data)
    print("Part 2: the decompressed length of the file is {}".format(length))

if __name__ == "__main__":
    main()
