def encode(password):
    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password

def decode(password):
    final = []
    for x in password:
        if x == "0":
            final.append("7")
        if x == "1":
            final.append("8")
        if x == "2":
            final.append("9")
        if x == "3":
            final.append("0")
        if x == "4":
            final.append("1")
        if x == "5":
            final.append("2")
        if x == "6":
            final.append("3")
        if x == "7":
            final.append("4")
        if x == "8":
            final.append("5")
        if x == "9":
            final.append("6")
    return "".join(final)