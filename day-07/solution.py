import re

class ABBA:
    def __init__(self):
        self.smfns = {
                        "seeking_abba_1": self.seeking_abba_1,
                        "seeking_abba_2": self.seeking_abba_2,
                        "seeking_abba_3": self.seeking_abba_3,
                        "seeking_abba_4": self.seeking_abba_4,
                        "seeking_terminator": self.seeking_terminator
                     }
        self.smfn = "seeking_abba_1"
        self.location = "supernet"
        self.abba_1 = "*"
        self.abba_2 = "*"
        self.supernet_abba = False
        self.hypernet_abba = False

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
            if self.location == "supernet":
                self.supernet_abba = True
                self.smfn = "seeking_terminator"
            else:
                self.hypernet_abba = True
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
                self.location = "hypernet"
                self.smfn = "seeking_abba_1"
            elif char == "]":
                self.location = "supernet"
                if self.supernet_abba == True:
                    self.smfn = "seeking_terminator"
                else:
                    self.smfn = "seeking_abba_1"
            else:
                self.smfns[self.smfn](char)
            if self.hypernet_abba == True:
                return False
        if self.supernet_abba == True:
            return True
        else:
            return False

class SSL:
    def __init__(self):
        self.smfns = {
                        "seeking_aba_1": self.seeking_aba_1,
                        "seeking_aba_2": self.seeking_aba_2,
                        "seeking_aba_3": self.seeking_aba_3,
                        "seeking_terminator": self.seeking_terminator,
                        "seeking_bab_1": self.seeking_bab_1,
                        "seeking_bab_2": self.seeking_bab_2,
                        "seeking_bab_3": self.seeking_bab_3,
                     }
        self.smfn = "seeking_aba_1"
        self.aba_1 = "*"
        self.aba_2 = "*"
        self.ssl_supported = False
        self.supernet_abas = []

    def seeking_aba_1(self, char):
        self.aba_1 = char
        self.smfn = "seeking_aba_2"

    def seeking_aba_2(self, char):
        if char != self.aba_1:
            self.aba_2 = char
            self.smfn = "seeking_aba_3"

    def seeking_aba_3(self, char):
        if char == self.aba_1:
            solution = "{}{}".format(self.aba_1, self.aba_2)
            self.supernet_abas.append(solution)
            self.aba_1 = self.aba_2
            self.aba_2 = char
        elif char == self.aba_2:
            self.aba_1 = char
            self.smfn = "seeking_aba_2"
        else:
            self.aba_1 = self.aba_2
            self.aba_2 = char
            self.smfn = "seeking_aba_3"

    def seeking_terminator(self, char):
        return

    def seeking_bab_1(self, char):
        if char == self.aba_2:
            self.smfn = "seeking_bab_2"

    def seeking_bab_2(self, char):
        if char == self.aba_1:
            self.smfn = "seeking_bab_3"
        elif char != self.aba_2:
            self.smfn = "seeking_bab_1"

    def seeking_bab_3(self, char):
        if char == self.aba_2:
            self.ssl_supported = True
        else:
            self.smfn = "seeking_bab_1"

    def evaluate(self, address):
        sequences = re.split("[\[\]]", address)
        supernet_sequences = []
        hypernet_sequences = []
        while len(sequences) > 1:
            supernet_sequences.append(sequences.pop())
            hypernet_sequences.append(sequences.pop())
        supernet_sequences.append(sequences.pop())

        for sequence in supernet_sequences:
            self.smfn = "seeking_aba_1"
            for j in range(len(sequence)):
                self.smfns[self.smfn](sequence[j])

        for sequence in hypernet_sequences:
            for solution in self.supernet_abas:
                self.aba_1 = solution[0]
                self.aba_2 = solution[1]
                self.smfn = "seeking_bab_1"
                for j in range(len(sequence)):
                    self.smfns[self.smfn](sequence[j])
                    if self.ssl_supported == True:
                        return True

        return False

def main():
    abba_sum = 0
    ssl_sum = 0
    file = open("puzzle-input.txt", "r")
    #file = open("p2-short-input.txt", "r")
    for line in file:
        abba = ABBA()
        if abba.evaluate(line.strip()) == True:
            abba_sum += 1
        ssl = SSL()
        if ssl.evaluate(line.strip()) == True:
            ssl_sum += 1

    print("Part 1: {} IPs support TLS".format(abba_sum))
    print("Part 2: {} IPs support SSL".format(ssl_sum))

if __name__ == "__main__":
    main()
