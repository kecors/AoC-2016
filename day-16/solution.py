LENGTH = 272

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

def main():
    data = open("puzzle-input.txt", "r").read().strip()
    while len(data) < LENGTH:
        data = generate(data)
    data = data[:LENGTH]

    data = checksum(data)
    while len(data) % 2 == 0:
        data = checksum(data)

    print("Part 1: the correct checksum is {}".format(data))

if __name__ == "__main__":
    main()
