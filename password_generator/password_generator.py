#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
import random

def generate_password(length):
    """Generate a random password of a given length."""
    # The password will be composed of printable ascii characters
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the given length
    password = ''.join(random.choice(chars) for i in range(length))
    return password


length = int(input("what length should your password be: "))
password = generate_password(length)
print("Generated password:", password)