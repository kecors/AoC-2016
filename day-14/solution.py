import hashlib
import re

SALT = "cuanljph"

def find_three(start):
    index = start
    while True:
        m = hashlib.md5()
        m.update("{}{}".format(SALT, index))
        digest = m.hexdigest()
        match = re.search(r'(.)\1\1', digest)
        if match:
            return(index, match.group(1))
        index += 1

def find_five(start, char):
    index = start
    while index <= (start + 1000):
        md5 = hashlib.md5()
        md5.update("{}{}".format(SALT, index))
        digest = md5.hexdigest()
        match = re.search(r'(%s)\1\1\1\1' % char, digest)
        if match:
            return True
        index += 1
    return False

def main():
    keys = 0
    j = -1
    while keys < 64:
        (j, c) = find_three(j+1)
        z = find_five(j+1, c)
        if z == True:
            keys += 1

    p1_result = j
    print("Part 1: index {} produces the 64th one-time pad key".format(p1_result))

if __name__ == "__main__":
    main()
