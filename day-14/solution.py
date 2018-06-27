import hashlib
import re
from collections import deque

class State:
    SALT = "cuanljph"

    def __init__(self, key_stretching_flag):
        self.hashes = deque()
        self.keys = []
        self.key_stretching_flag = key_stretching_flag

    def generate_hash(self, index):
        m = hashlib.md5()
        m.update("{}{}".format(State.SALT, index))
        digest = m.hexdigest()
        if self.key_stretching_flag == True:
            for _ in range(2016):
                m = hashlib.md5()
                m.update(digest)
                digest = m.hexdigest()
        self.hashes.append(digest)

    def compute(self):
        index = 0
        while True:
            if len(self.hashes) == 0:
                self.generate_hash(index)
            hash3 = self.hashes.popleft()
            match = re.search(r'(.)\1\1', hash3)
            if match:
                char = match.group(1)
                j = 0
                while j < 1000:
                    if len(self.hashes) <= j:
                        self.generate_hash(index + 1 + j)
                    hash5 = self.hashes[j]
                    match = re.search(r'(%s)\1\1\1\1' % char, hash5)
                    if match:
                        self.keys.append((index, hash3))
                        break
                    j += 1

            if len(self.keys) >= 64:
                (index, hash3) = self.keys.pop()
                return index

            index += 1

def main():
    state = State(False)
    p1_result = state.compute()
    print("Part 1: index {} produces the 64th one-time pad key".format(p1_result))
    state = State(True)
    p2_result = state.compute()
    print("Part 2: index {} now produces the 64th one-time pad key".format(p2_result))

if __name__ == "__main__":
    main()
