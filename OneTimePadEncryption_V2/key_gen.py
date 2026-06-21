import secrets
from utils import characters


def gen_key(msg):
    key = []
    for _ in range(len(msg)):
        key.append(secrets.choice(characters))

    return key