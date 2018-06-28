P1_LENGTH = 272
P2_LENGTH = 35651584

def generate(a):
    b = ''.join(map(lambda x: '0' if x == '1' else '1', a[::-1]))
    return a + '0' + b

def checksum(data):
    result = ''
    j = 0
    while j < len(data):
        if data[j] == data[j+1]:
            result += '1'
        else:
            result += '0'
        j += 2
    return result

def process(length):
    data = open("puzzle-input.txt", "r").read().strip()
    while len(data) < length:
        data = generate(data)
    data = data[:length]

    data = checksum(data)
    while len(data) % 2 == 0:
        data = checksum(data)

    return data

def main():
    p1_result = process(P1_LENGTH)
    print("Part 1: the correct checksum is {}".format(p1_result))
    p2_result = process(P2_LENGTH)
    print("Part 2: the correct checksum is {}".format(p2_result))

if __name__ == "__main__":
    main()
