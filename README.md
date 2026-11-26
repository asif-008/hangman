# Hangman

A Python terminal game inspired by freeCodeCamp.org’s *12 Beginner Python Projects*. The game picks a word from [the word list](words.py). You have six incorrect guesses to reveal it.

## Play

From the project directory, run `python main.py` with Python 3. Enter one letter at a time. A correct guess reveals every matching position; repeating a letter keeps your remaining lives intact.

For example, if the hidden word were **APPLE**, guessing **p** would reveal `- P P - -` with all six lives remaining. Guessing **z** next would leave the word as it is and reduce your lives to five.

At the end of a round, enter `y` for another word or any other response to exit. The game uses Python’s standard library.
