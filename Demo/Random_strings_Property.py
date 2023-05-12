from faker import Faker
import random
import string

fake = Faker()

def random_letter():
    return random.choice(string.ascii_letters)

def random_digit():
    return random.choice(string.digits)

def random_punctuation():
    return random.choice(string.punctuation)

def random_whitespace():
    return random.choice(string.whitespace)

def random_char():
    return random.choice(string.ascii_letters + string.digits + string.punctuation + ' ')

def random_str(length: int) -> str:
    result = ''
    for _ in range(length):
        space_prob = random.random()  # generate a random probability
        if space_prob < 0.2:
            result += ' '
        else:
            result += random_char()
    return result

def random_uppercase_string(n):
    return ''.join(random.choices(string.ascii_uppercase, k=n))

def random_lowercase_string(n):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def random_word(length = None):
    jumbled_chars = [char.upper() if random.randint(0, 1) else char.lower() for char in fake.word()]
    jumbled_word = ''.join(jumbled_chars)
    return jumbled_word

def empty_string(length = None):
    return ""
