
from utils import characters, ask_user
from key_gen import gen_key



def get_file():
    while True:
        filepath = input("Enter file path: ")
        try:
            with open(filepath, 'r+') as f:
                content = f.read()
                break

        except FileNotFoundError:
                print(f"File {filepath} not found. Verify filepath and try again.")
                continue

        except Exception as e:
                print(f"Error while reading file: {e}")
                continue

    return content

def save(content) -> None:
    while True:
        filepath = input("Enter file path or file name of the output file: ")
        confirmation = ask_user(f"Confirm filepath '{filepath}'?")
        if confirmation:
            break

    with open(filepath, 'w') as f:
        f.write("".join(content))


#Shift msg pos by pos char in key in characters
def encrypt_file() -> list:
    content = get_file()
    key = gen_key(content)

    indexes = []
    for c in key:
        index = characters.index(c)
        indexes.append(index)


    encrypted_content = []
    i = 0
    for c in content:
        if c in characters:

            content_idx = characters.index(c)
            encrypted_content.append(characters[(content_idx+ indexes[i])%len(characters)])
            i += 1
        else:
            encrypted_content.append(c)

    print(f"Your key: {''.join(key)}")
    print(f"Your encrypted message: {''.join(encrypted_content)}")

    print(f"Content length: {len(content)}")
    print(f"length of encrypted message: {len(encrypted_content)}")

    save(encrypted_content)

    return encrypted_content

def decrypt_file() -> list:
    content = get_file()
    decrypted_content = []

    key = input(f"Enter key: ")
    idx = 0
    for key_c, encrypted_c in zip(key, content):
        if encrypted_c in characters:
            key_idx = characters.index(key[idx])
            encrypted_idx = characters.index(encrypted_c)

            decrypted_content.append(characters[(encrypted_idx - key_idx) % len(characters)])
            idx += 1
        else:
            decrypted_content.append(encrypted_c)

    save(decrypted_content)

    return decrypted_content

