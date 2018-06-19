class State:
    def __init__(self):
        self.smfns = {
                        "seeking_abba_1": self.seeking_abba_1,
                        "seeking_abba_2": self.seeking_abba_2,
                        "seeking_abba_3": self.seeking_abba_3,
                        "seeking_abba_4": self.seeking_abba_4,
                        "seeking_terminator": self.seeking_terminator
                     }
        self.smfn = "seeking_abba_1"
        self.location = "outer"
        self.abba_1 = "*"
        self.abba_2 = "*"
        self.outer_abba = False
        self.inner_abba = False

    def seeking_abba_1(self, char):
        self.abba_1 = char
        self.smfn = "seeking_abba_2"

    def seeking_abba_2(self, char):
        if char != self.abba_1:
            self.abba_2 = char
            self.smfn = "seeking_abba_3"

    def seeking_abba_3(self, char):
        if char == self.abba_2:
            self.smfn = "seeking_abba_4"
        else:
            self.abba_1 = self.abba_2
            self.abba_2 = char
            self.smfn = "seeking_abba_3"

    def seeking_abba_4(self, char):
        if char == self.abba_1:
            if self.location == "outer":
                self.outer_abba = True
                self.smfn = "seeking_terminator"
            else:
                self.inner_abba = True
        else:
            self.abba_1 = self.abba_2
            self.abba_2 = char
            self.smfn = "seeking_abba_3"

    def seeking_terminator(self, char):
        return

    def evaluate(self, address):
        for j in range(len(address)):
            char = address[j]
            if char == "[":
                self.location = "inner"
                self.smfn = "seeking_abba_1"
            elif char == "]":
                self.location = "outer"
                if self.outer_abba == True:
                    self.smfn = "seeking_terminator"
                else:
                    self.smfn = "seeking_abba_1"
            else:
                self.smfns[self.smfn](char)
            if self.inner_abba == True:
                return False
        if self.outer_abba == True:
            return True
        else:
            return False

def main():
    sum = 0
    file = open("puzzle-input.txt", "r")
    for line in file:
        state = State()
        if state.evaluate(line.strip()) == True:
            sum += 1

    print("Part 1: {} IPs support TLS".format(sum))

if __name__ == "__main__":
    main()
