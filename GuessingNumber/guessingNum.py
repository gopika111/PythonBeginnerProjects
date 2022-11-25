import random


def generate_number(upperlimit):
    number_generated = random.randint(1, int(upperlimit))
    return number_generated


def guessing_number(number_generated, no_of_chances_req, upperlimit):
    current_chance = 0
    lower_limit = 1
    while current_chance <= no_of_chances_req:
        guessed_number = int(input("Enter your guess : "))
        average = int((lower_limit + upperlimit)/2)
        if guessed_number == number_generated:
            print("Yayy you guessed it right!!!")
            break
        elif number_generated <= average:
            upperlimit = average
            print(f"Clue: Number to be guessed is in tha range of {lower_limit} and {upperlimit}")
        else:
            lower_limit = average
            print(f"Clue: Number generated is in the range of {lower_limit} and {upperlimit}")
    current_chance +=1
    if current_chance == no_of_chances_req+1:
        print("Game Over!!!")
        print(f"The number is {number_generated}")


upperlimit = int(input("Enter Upper Limit : "))
no_of_chances_req = int(input("Enter No of chances required : "))

number_generated = generate_number(upperlimit)
guessing_number(number_generated, no_of_chances_req, upperlimit)
