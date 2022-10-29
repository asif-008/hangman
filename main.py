import random
from words import words

word = random.choice(words).upper()  # choose a word for user to play with


def hangman(name):

    lives = 6
    used_letters = ""
    current_word_list = []

    for aletter in name:
        current_word_list.append("-")

    copy_name = []
    for a_letter in name:
        copy_name.append(a_letter)

    while lives > 0:
        current_word = ""
        for item in current_word_list:
            current_word = current_word +" " + item

        print("Lives left: " + str(lives)+"\n"+"Letters used: "+str(used_letters))
        print("Current word: "+str(current_word))
        letter = input("Guess a letter: ").upper()

        if used_letters.__contains__(letter) == True:
            print("you used it already")
            continue
        else:
            used_letters = used_letters+" "+str(letter)

        if letter in copy_name:
            x = 0
            for item in copy_name:
                if item == letter:
                    current_word_list[x] = letter
                x = x + 1

            if current_word_list == copy_name:
                print("you guessed right! The word was "+str(name))
                user_choice = input("Do you want to play again? If yes, input 'y', or input anything else: ")
                if user_choice != 'y':
                    exit()
                else:
                    new_word = random.choice(words).upper()
                    hangman(new_word)

        else:
            lives = lives - 1
            print("your letter is not in the word")

    if lives == 0:
        print("Sorry, you died. The word was: " + str(name))
        user_choice = input("Do you want to play again? If yes, input 'y', or input anything else: ")
        if user_choice == 'y':
            new_word = random.choice(words).upper()
            hangman(new_word)
        else:
            exit()


hangman(word)
