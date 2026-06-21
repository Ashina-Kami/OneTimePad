import string

characters = list(string.ascii_letters + string.digits + string.punctuation + " ")

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

