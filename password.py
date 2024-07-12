import random
import string

def generate_random_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)
