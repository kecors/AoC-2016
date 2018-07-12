import re

class State:
    def __init__(self, instructions):
        self.instructions = instructions

    def init(self, a):
        self.a = a
        self.b = 0
        self.c = 0
        self.d = 0
        self.ip = 0 # instruction pointer
        self.expected_signal = 0

    def execute(self):
        while True:
            if self.ip < 0 or self.ip >= len(self.instructions):
                break
            instruction = self.instructions[self.ip]
            #print("{} {} {} {} : {}".format(self.a, self.b, self.c, self.d, self.ip))
            #print self.instructions
            #print self.instructions[self.ip]
            m = re.match("^out ([a-d])$", instruction)
            if m:
                register = m.group(1)
                value = self.__dict__[register]
                if value != self.expected_signal:
                    return
                if self.expected_signal == 0:
                    self.expected_signal = 1
                else:
                    self.expected_signal = 0
                self.ip += 1
                continue
            m = re.match("^out (-?\d+)$", instruction)
            if m:
                value = int(m.group(1))
                if value != self.expected_signal:
                    return
                if self.expected_signal == 0:
                    self.expected_signal = 1
                else:
                    self.expected_signal = 0
                self.ip += 1
                continue
            m = re.match("^cpy (-?\d+) ([a-d])$", instruction)
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
            m = re.match("^jnz (\d+) ([a-d])$", instruction)
            if m:
                flag, register = int(m.group(1)), m.group(2)
                if flag == 0:
                    self.ip += 1
                else:
                    self.ip += self.__dict__[register]
                continue
            m = re.match("^tgl ([a-d])$", instruction)
            if m:
                register = m.group(1)
                offset = getattr(self, register)
                if offset == 0:
                    self.instructions[self.ip].replace("tgl", "inc")
                    self.ip += 1
                    continue
                target_ip = self.ip + offset
                if target_ip < 0 or target_ip >= len(self.instructions):
                    self.ip += 1
                    continue
                target_instr = self.instructions[target_ip]
                if target_instr.find("inc") is not -1:
                    new_instruction = target_instr.replace("inc", "dec")
                elif target_instr.find("dec") is not -1:
                    new_instruction = target_instr.replace("dec", "inc")
                elif target_instr.find("tgl") is not -1:
                    new_instruction = target_instr.replace("tgl", "inc")
                elif target_instr.find("jnz") is not -1:
                    new_instruction = target_instr.replace("jnz", "cpy")
                elif target_instr.find("cpy") is not -1:
                    new_instruction = target_instr.replace("cpy", "jnz")
                else:
                    new_instruction = target_instr
                self.instructions[target_ip] = new_instruction
                self.ip += 1
                continue

def main():
    file = open("puzzle-input.txt", "r")
    contents = file.read()
    state = State(contents.strip().split("\n"))
    x = 0
    while True:
        state.init(x)
        state.execute()
        print("{} failed".format(x))
        x += 1

if __name__ == "__main__":
    main()
