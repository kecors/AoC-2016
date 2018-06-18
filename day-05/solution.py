import hashlib

def main():
    door_id = "reyedfim"
    password = ""
    x = 0
    while len(password) < 8:
        word = "{}{}".format(door_id, x)
        m = hashlib.md5()
        m.update(word)
        digest = m.hexdigest()
        if digest.startswith("00000"):
            password += digest[5]
        x += 1
    print("The password is {}".format(password))

if __name__ == "__main__":
    main()
