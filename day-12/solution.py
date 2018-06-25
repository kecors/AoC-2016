import re

class State:
    def __init__(self, instructions):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.instructions = instructions
        self.ip = 0 # instruction pointer

    def execute(self):
        while True:
            if self.ip < 0 or self.ip >= len(self.instructions):
                break
            instruction = self.instructions[self.ip]
            m = re.match("^cpy (\d+) ([a-d])$", instruction)
            if m:
                value, register = int(m.group(1)), m.group(2)
                self.__dict__[register] = value
                self.ip += 1
                continue
            m = re.match("^cpy ([a-d]) ([a-d])$", instruction)
            if m:
                source, destination = m.group(1), m.group(2)
                self.__dict__[destination] = self.__dict__[source]
                self.ip += 1
                continue
            m = re.match("^inc ([a-d])$", instruction)
            if m:
                register = m.group(1)
                self.__dict__[register] += 1
                self.ip += 1
                continue
            m = re.match("^dec ([a-d])$", instruction)
            if m:
                register = m.group(1)
                self.__dict__[register] -= 1
                self.ip += 1
                continue
            m = re.match("^jnz ([a-d]) (-?\d+)$", instruction)
            if m:
                flag, distance = m.group(1), int(m.group(2))
                if self.__dict__[flag] == 0:
                    self.ip += 1
                else:
                    self.ip += distance
                continue
            m = re.match("^jnz (\d+) (-?\d+)$", instruction)
            if m:
                flag, distance = int(m.group(1)), int(m.group(2))
                if flag == 0:
                    self.ip += 1
                else:
                    self.ip += distance
                continue

def main():
    file = open("puzzle-input.txt", "r")
    contents = file.read()
    state = State(contents.strip().split("\n"))
    state.execute()
    print("Part 1: the value left in register a is {}".format(state.a))

if __name__ == "__main__":
    main()
