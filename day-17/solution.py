import hashlib
import heapq

def is_room(path):
    vertical = path.count('D') - path.count('U')
    if vertical < 0 or vertical > 3:
        return False
    horizontal = path.count('R') - path.count('L')
    if horizontal < 0 or horizontal > 3:
        return False
    return True

def is_vault(path):
    vertical = path.count('D') - path.count('U')
    horizontal = path.count('R') - path.count('L')
    if vertical == 3 and horizontal == 3:
        return True
    return False

class State:
    def __init__(self, passcode):
        self.passcode = passcode
        self.directions = ['U', 'D', 'L', 'R']

    def find_open_doors(self, path):
        result = []
        m = hashlib.md5()
        m.update(self.passcode + path)
        digest = m.hexdigest()
        for x in range(len(self.directions)):
            if "bcdef".count(digest[x]) == 1:
                newpath = path + self.directions[x]
                if is_room(newpath):
                    result.append(newpath)
        return result

    def process(self):
        paths = []
        heapq.heappush(paths, (0, ""))
        while True:
            (distance, path) = heapq.heappop(paths)
            newpaths = self.find_open_doors(path)
            for newpath in newpaths:
                if is_vault(newpath):
                    return newpath
                heapq.heappush(paths, (len(newpath), newpath))

def main():
    passcode = open("puzzle-input.txt", "r").read().strip()
    state = State(passcode)
    p1_result = state.process()
    print("Part 1: the shortest path to reach the vault is {}".format(p1_result))

if __name__ == "__main__":
    main()
