
# One Time Pad (OTP) over 95 characters


from utils import characters, ask_user
from key_gen import gen_key
from file_encryption import encrypt_file, decrypt_file




def get_message():
    while True:
        try:
            msg = input("Enter message to encrypt: ")
            print(f"Confirm message: {msg}")
            confirmation = ask_user("Encrypt this message?")
            if confirmation:
                return msg
        except Exception as e:
            print(f"An error occurred: {e}")
            continue


# Shift msg pos by pos char in key in characters
def encrypt_message():
    msg = get_message()
    key = gen_key(msg)

    print(f"length msg to encrypt: {len(msg)}")

    indexes = []
    for c in key:
        index = characters.index(c)
        indexes.append(index)


    encrypted_msg = []
    i = 0
    for c in msg:
        if c in characters:

            msg_idx = characters.index(c)
            encrypted_msg.append(characters[(msg_idx + indexes[i])%len(characters)])
            i += 1

    print(f"Your key: {''.join(key)}")
    print(f"Your encrypted message: {''.join(encrypted_msg)}")

    print(f"length of encrypted message: {len(encrypted_msg)}")

    return encrypted_msg


def decrypt_message():
    decrypted_msg = []
    key = input(f"Enter key: ")
    encrypted_msg = input(f"Enter encrypted message: ")

    for key_c, encrypted_c in zip(key, encrypted_msg):
        if encrypted_c in characters:

            key_idx = characters.index(key_c)
            encrypted_idx = characters.index(encrypted_c)

            decrypted_msg.append(characters[(encrypted_idx - key_idx)%len(characters)])

    print(f"Decrypted message: {''.join(decrypted_msg)}")

    return decrypted_msg

def encrypt_menu():
    choices = {
        1: encrypt_message,
        2: encrypt_file,
        3: None
    }
    while True:
        print("1. Encrypt message")
        print("2. Encrypt file")
        print("3. Back")
        try:
            choice = int(input("Choose your choice: "))
            if choice not in choices:
                print("Invalid choice")
                continue
            break

        except ValueError:
            print("Choice must be integer")

    if choice == 3:
        return

    choices[choice]()

def decrypt_menu():
    choices = {
        1: decrypt_message,
        2: decrypt_file,
        3: None
    }

    while True:
        print("1. Decrypt message")
        print("2. Decrypt file")
        print("3. Back")
        try:
            choice = int(input("Choose your choice: "))
            if choice not in choices:
                print("Invalid choice")
                continue
            break
        except ValueError:
            print("Choice must be integer")
    if choice == 3:
        return

    choices[choice]()

def main():
    choices = {
        1: encrypt_menu,
        2: decrypt_menu,
        3: None
    }

    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        try:
            choice = int(input("Choose your choice: "))

            if choice not in choices:
                print("Invalid choice")
                continue
            if choice == 3:
                print("Goodbye! :)")
                quit()

            choices[choice]()

        except ValueError:
            print("Choice must be integer")


if __name__ == '__main__':
    main()