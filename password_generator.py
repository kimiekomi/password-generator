#!/usr/local/bin/python3

import random

def password_generator(number_of_letters, number_of_numbers=1, number_of_special_characters=1):

    letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_characters = "~!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?"

    password = ""

    for i in range (number_of_letters):
        random_index = random.randrange(len(letters))
        password += letters[random_index]

    for i in range (number_of_numbers):
        random_index = random.randrange(len(numbers))
        password += numbers[random_index]

    for i in range (number_of_special_characters):
        random_index = random.randrange(len(special_characters))
        password += special_characters[random_index]
    
    # password = random.shuffle(password)

    password = "".join(random.sample(password,len(password)))

    return password


if __name__ == "__main__":
    print(password_generator(8, 2, 2))
    print(password_generator(9, 2, 2))
    print(password_generator(10, 2, 2))
    print(password_generator(11, 2, 2))
    print(password_generator(12, 2, 2))
