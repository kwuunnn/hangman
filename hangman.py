def diagram(stage):
    stages = [
        "------------",
        """
        ------------
        |
        |
        |
        |
        |
        |
        """,
        """
        ------------
        |     |
        |
        |
        |
        |
        |
        """,
        """
        ------------
        |     |
        |     O
        |
        |
        |
        |
        """,

        """
        ------------
        |     |
        |     O
        |     |
        |     |
        |     
        |
        """,

        """
        ------------
        |     |
        |     O
        |    /|
        |     |
        |     
        |
        """,

        """
        ------------
        |     |
        |     O
        |    /|\\
        |     |
        |     
        |
        """,

        """
        ------------
        |     |
        |     O
        |    /|\\
        |     |
        |    / 
        |
        """,

        """
        ------------
        |     |
        |     O
        |    /|\\
        |     |
        |    / \\
        |
        """
    ]
    display = stages[stage - 1]
    return display


from english_words import english_words_alpha_set
import random


def valid_word():
    word_list = list(english_words_alpha_set)
    word = random.choice(word_list)

    while '-' in word or ' ' in word or len(word) < 5:
        word = random.choice(word_list)

    return word.upper()


def hangman(word):
    word_length = len(word)
    word_letters = list(word)
    wrong_letters = []
    used_letters = []

    print('Let\'s play hangman!\n')
    blanks = '_' * word_length
    print(f'The word has {word_length} letters. {blanks}\n')

    result = ['_' for i in range(word_length)]

    while '_' in result:
        guess = str(input('Guess a letter: \n').upper())

        if guess.isalpha() == False or len(guess) != 1:
            print(f'Sorry, your guess \'{guess}\' is invalid. Please make sure your guess is a letter in the alphabet.')

        elif guess in used_letters:
            print(f'Sorry, you have guessed the letter {guess} before. Please try again.\n')

        elif guess in word_letters:
            print(f'Good guess! {guess} is in the word.\n')

            for index, letter in enumerate(word):
                if guess == letter:
                    result[index] = guess

        else:
            used_letters.append(guess)
            wrong_letters.append(guess)
            print(f'Oh no. Unfortunately {guess} is not in the word.\n')
            wrong_tries = len(wrong_letters)
            print(f'Hangman diagram:\n {diagram(wrong_tries)}\n')

            if wrong_tries == 9:
                print(f'Sorry, you lost! The word was {word}. Try again next time!')
                break

        print(f'You have used the letters {used_letters} so far.')
        guessed_word = ''.join(result)
        print(f'Your guess so far: {guessed_word}\n')
        if guessed_word == word:
            print('Congrats! You have guessed the word correctly!')


def main():
    word = valid_word()
    hangman(word)
    option = str(input('Would you like to play again? (Y/N): ').upper())
    while option not in ['Y', 'N']:
        option = str(input('Would you like to play again? (Y/N): ').upper())
    if option == 'Y':
        main()
    elif option == 'N':
        print('Thanks for playing. Try again next time!')


if __name__ == "__main__":
    main()
