import random

games = ["Chess", "Rubik's Cube", "Badminton", "Table Tennis"]

print(random.choice(games))

random_game = random.choice(games)

random_madlib = f"I love playing {random_game}. " \
                f"Playing {random_game} keeps me happy."

print(random_madlib)