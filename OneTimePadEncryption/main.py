
# One Time Pad (OTP) over 95 characters

import string
import secrets

characters = list(string.ascii_letters + string.digits + string.punctuation)


def gen_key(msg):
    key = []
    for _ in range(len(msg)):
        key.append(secrets.choice(characters))

    #for c in msg:
    #    if c in characters:
    #        key.append(secrets.choice(characters))
    #print(f"Your key is {''.join(key)}")

    return key


def ask_user(prompt:str):
    while True:
        confirmation = input(f"{prompt}(y/n)?")
        if confirmation not in ['y', 'n']:
            print('Please respond with "y" or "n"')
            continue

        if confirmation == 'y':
            return True
        else:
            return False


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


#Shift msg pos by pos char in key in characters
def encrypt_message():
    msg = get_message()
    key = gen_key(msg)

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
        #else:
        #    encrypted_msg.append(c)

    print(f"Your key: {''.join(key)}")
    print(f"Your encrypted message: {''.join(encrypted_msg)}")

    return encrypted_msg


def decrypt_message():
    decrypted_msg = []
    key = input(f"Enter key: ")
    encrypted_msg = input(f"Enter encrypted message: ")

    for key_c, encrypted_c in zip(key, encrypted_msg):
        #print(f"{key_c}: {''.join(encrypted_c)}")
        if encrypted_c in characters:

            key_idx = characters.index(key_c)
            encrypted_idx = characters.index(encrypted_c)

            decrypted_msg.append(characters[(encrypted_idx - key_idx)%len(characters)])

    # Add space after punctuation
    # Add space before Maj
    result = []
    for i, c in enumerate(decrypted_msg):
        if i != 0 and c.isupper():
            result.append(' ')

        result.append(c)

    print(f"Decrypted message: {''.join(result)}")

    return decrypted_msg


def main():
    choices = {
        1: encrypt_message,
        2: decrypt_message,
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