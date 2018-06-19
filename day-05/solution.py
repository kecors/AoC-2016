import hashlib

def main():
    door_id = "reyedfim"
    password_p1 = ""
    password_p2 = ['*','*','*','*','*','*','*','*']
    p1_flag = True
    p2_flag = True
    p2_counter = 0
    x = 0
    while p1_flag or p2_flag:
        word = "{}{}".format(door_id, x)
        m = hashlib.md5()
        m.update(word)
        digest = m.hexdigest()
        if p1_flag and digest.startswith("00000"):
            #print("P1: {}, {}".format(digest, word))
            password_p1 += digest[5]
            if len(password_p1) == 8:
                p1_flag = False
        if p2_flag and digest.startswith("00000") and digest[5] < '8':
            #print("P2: {}, {}".format(digest, word))
            index = int(digest[5])
            if password_p2[index] == '*':
                password_p2[index] = digest[6]
                p2_counter += 1
            if p2_counter == 8:
                p2_flag = False
        x += 1
    print("Part 1: The password is {}".format(password_p1))
    print("Part 2: the password is {}".format(''.join(password_p2)))

if __name__ == "__main__":
    main()
