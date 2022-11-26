import random


def guessingNumber(number_given, no_of_tries, upper_limit):
    current_chance = 1
    lower_limit = 1
    while current_chance <= no_of_tries:
        guessed_number = random.randint(lower_limit, upper_limit)
        if guessed_number == number_given:
            print("Number guessed by comp is right.")
            break
        elif guessed_number > number_given:
            upper_limit = guessed_number
            print(f"Guessed Number is {guessed_number} but it was high")
        else:
            lower_limit = guessed_number
            print(f"Guessed Number is {guessed_number} but it was low")
        current_chance += 1


number_given = int(input("Enter the number to be guessed by computer : "))
no_of_tries = int(input("No of tries : "))
upper_limit = int(input("Upper Limit : "))
guessingNumber(number_given, no_of_tries, upper_limit)
