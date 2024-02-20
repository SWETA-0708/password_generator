import random
import string

def password_generator(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters = string.ascii_lowercase  # lowercase letters are always included

    if use_uppercase:
        characters += string.ascii_uppercase  # include uppercase letters

    if use_numbers:
        characters += string.digits  # include numbers

    if use_symbols:
        characters += string.punctuation  # include symbols

    # Generate the password using random.choices()
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage
password = password_generator()
print("Generated Password:", password)
