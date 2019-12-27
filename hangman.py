import random
from string import ascii_lowercase
import sys

attempts = 8
headline = 'H A N G M A N'
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
f_word = '-' * len(word)
print("H A N G M A N")


def find_letter(letter, string):
    word_list = list(string)
    indexes = []
    index = 0
    for char in word_list:
        if char == letter:
            indexes.append(index)
            index += 1
        else:
            index += 1
    return indexes


def checker(u_input):
    if len(u_input) != 1:
        print('You should print a single letter')
        return True
    elif u_input not in ascii_lowercase:
        print('It is not an ASCII lowercase letter')
        return True


while True:
    choice = input('Type "play" to play game, "exit" to quit: ')
    print(choice)
    if choice == 'exit':
        sys.exit()
    elif choice == 'play':
        break
    else:
        continue

typed_letters = []
while attempts > 0:
    if f_word == word:
        print('You guessed the word!')
        print('You survived!')
        break
    print('')
    print(f_word)
    letter = input('Input a letter: ')
    print(letter)
    if checker(letter):
        continue
    if letter in typed_letters:
        print('You already typed this letter')
        continue
    if letter in word:
        if letter in f_word:
            print('You already typed this letter')
            continue
        f_word = list(f_word)
        indexes = find_letter(letter, word)
        for index in indexes:
            f_word[index] = letter
        if f_word == word:
            print('You guessed the word!')
            print('You survived!')
            break
    else:
        print('No such letter in the word')
        attempts -= 1
        if attempts == 0:
            print('You are hanged!')
            break
    f_word1 = ''
    for i in f_word:
        f_word1 += str(i)
    f_word = f_word1
    typed_letters.append(letter)

