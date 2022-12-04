import random
import word_list


def play_hangman():
    chosen_word = random.choice(word_list.list_of_words)

    no_of_clues = len(chosen_word)/2 -1

    clues = []

    while len(clues) < no_of_clues:
        index = random.randint(0, len(chosen_word)-1)
        if index not in clues:
            clues.append(index)

    given_string = ""
    changed_word = ""
    for i in range(0, len(chosen_word)):
        if i not in clues:
            given_string += "_"
            changed_word += chosen_word[i]
        else:
            given_string += chosen_word[i]
            changed_word += "_"

    print(f"Word to be guessed : {given_string}")
    print("Start Guessing")
    no_of_guesses = len(chosen_word) - no_of_clues + 3
    current_guess = 0
    while current_guess <= no_of_guesses:
        letter = input("Enter the letter : ")
        if letter in changed_word:
            req_index = changed_word.index(letter)
            given_string = given_string[:req_index] + letter + given_string[req_index+1:]
            changed_word = changed_word[:req_index] + "_" + changed_word[req_index+1:]
            if chosen_word == given_string:
                print("Yayy!!! You guessed it right")
                break
            else:
                print(f"Word to be guessed : {given_string}")
                print("You are one step ahead")
                print(f"Try guessing the word {given_string}")
        else:
            print("Try guessing another letter...")
        current_guess += 1
        if current_guess > no_of_guesses:
            print(f"Game Over!!! The right word was {chosen_word}")


play_hangman()
