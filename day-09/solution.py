import re

def main():
    data = open("puzzle-input.txt", "r").read().strip()
    j = 0
    length = 0
    while j < len(data):
        if data[j] == '(':
            m = re.match("^\(([0-9]+)x([0-9]+)\).*$", data[j:])
            if m:
                a, b = m.group(1), m.group(2)
                length += int(a) * int(b)
                j += len(a) + len(b) + 3 + int(a)
            else:
                length += 1
                j += 1
        else:
            length += 1
            j += 1
    print("Part 1: the decompressed length of the file is {}".format(length))

if __name__ == "__main__":
    main()
