
import random
import hangman_words
import hangman_art

stages = hangman_art.stages
logo = hangman_art.logo


word_list = hangman_words.word_list

word = word_list[random.randint(0, len(word_list) - 1)]
word = list(word)
empty_word = ['_' for i in range(len(word))]
lives = 6
print(logo)
print(stages[lives])
print(' '.join(empty_word))

while '_' in empty_word:
  
  letter_choice = input('Pick a letter: ')
  if letter_choice in empty_word:
    print(f"You've already used the letter {letter_choice}")
  for index, letter in enumerate(word):
    if letter_choice.lower() == letter:
      empty_word[index] = letter_choice
  print(' '.join(empty_word))
  
  if ''.join(word).find(letter_choice) == -1:
    print(f"You guessed {letter_choice}. {letter_choice} is not in the word. You lose a life!")
    lives -= 1
  print(stages[lives])
  print(' '.join(empty_word))
  if lives == 0:
    joined_word = ''.join(word)
    print('You Lose!')
    print(f'The word was: {joined_word}')
    break
  if '_' not in empty_word:
    print('You win!')
    break
  
