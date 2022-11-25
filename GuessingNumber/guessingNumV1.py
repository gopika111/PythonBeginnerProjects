import random


def guess_the_number(upper_limit):
    number_generated = random.randint(1, upper_limit)
    guessed_number = 0
    while number_generated != guessed_number:
        guessed_number = int(input("Guess the number : "))
        if guessed_number == number_generated:
            print("Yayy!!! You guessed it right")
        elif guessed_number < number_generated:
            print("Sorry.. the number is too low")
        else:
            print("Sorry..the number is too high")


upper_limit = int(input("Enter the upper limit : "))
guess_the_number(upper_limit)