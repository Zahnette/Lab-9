def encode(password):
    return ''.join(str((int(char) + 3) % 10) for char in password)

def decode(password):
    return ''.join(str((int(char) - 3) % 10) for char in password)

def main():
    encoded_password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if encoded_password:
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            else:
                print("No encoded password stored.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
