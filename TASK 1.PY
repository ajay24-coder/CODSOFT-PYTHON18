#Password generator
import random
import string

def password_generator(length = 15, mix_types = True):
    chars = string.ascii_letters + string.digits + string.punctuation
    if mix_types:
        #Please Ensure at least one of each character type10
        password = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]
        #fill the remaining portin of password
        for _ in range(length - 4):
            password.append(random.choice(chars))
    else:
        # Use the full character set without ensuring mix
        password = [random.choice(chars) for _ in range(length)]
    # Now shuffle list to avoid first three character always being in same character type order
    random.shuffle(password)
    return ''.join(password)
length = int(input("Enter desired password length (min 4):")or 15)
mix_types = input("Ensure mix of character types? (y/n):").lower() == 'y'
print("Generated password:", password_generator(length, mix_types))             
            