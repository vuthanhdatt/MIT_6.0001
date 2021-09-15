# Problem Set 2, hangman.py
# Name: Vu Thanh Dat
# Collaborators: No
# Time spent: ...

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import time
start_time = time.time()
import random
import string

WORDLIST_FILENAME = "ps2\words.txt"


def load_words():
   """
   Returns a list of valid words. Words are strings of lowercase letters.
   
   Depending on the size of the word list, this function may
   take a while to finish.
   """
   print("Loading word list from file...")
   # inFile: file
   inFile = open(WORDLIST_FILENAME, 'r')
   # line: string
   line = inFile.readline()
   # wordlist: list of strings
   wordlist = line.split()
   print("  ", len(wordlist), "words loaded.")
   return wordlist


def choose_word(wordlist):
   """
   wordlist (list): list of words (strings)
   
   Returns a word from wordlist at random
   """
   return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
   """
   secret_word: strings
   letters_guessed: list
   
   Return True if all letters of secret_word are in letter_guessed
   """
   check = 0
   for i in secret_word:
      if i not in letters_guessed:
         check +=1
   if check != 0:
      return False
   return True


def get_guessed_word(secret_word, letters_guessed):
   """
   secret_word: strings
   letters_guessed: list
   
   Returns a string that is comprised of letters and underscores,
   based on what letters in letters_guessed​ are in ​secret_word to display for user
   """
   
   word_display = ''
   for i in secret_word:
      if i in letters_guessed:
         word_display += i
      else:
         word_display += '_ '
   return word_display
    

def get_available_letters(letters_guessed):
   
   s = string.ascii_lowercase
   for i in letters_guessed:
      s = s.replace(i,'')
   return s
      
def unique(secret_word):
   k=0
   s = string.ascii_lowercase
   for i in  s:
      if i in secret_word:
         k+=1
   return k

def hangman(secret_word):
   guess_left = 6
   warming_left = 3
   letters_guess =[]
   dash = '-'*20

   print('Welcome to Hangman')
   print(f"I'm thinking of a word that is {len(secret_word)} letters long")
   print(f'You have {warming_left} warmings left')
   print(dash)
   
   while(guess_left>0):
      if is_word_guessed(secret_word,letters_guess):
         print('Congratulations, you won!')
         print(f"Your total score for this game:{guess_left*unique(secret_word)}")
         break
      print(guess_left)
      print(f'You have {guess_left} guesses left')
      print(f"Available letters:{get_available_letters(letters_guess)}")
      character = input('Please guess a letter:')
      
      if len(character) !=1 or str.isalpha(character) == False:
         if warming_left ==0:
            guess_left -=1
            print(f'Oops! That is not a valid letter.You have no warnings left so you lose one guess')
            print(dash)
         else:
            warming_left -=1
            print(f'Oops! That is not a valid letter. You have {warming_left} warnings left:{get_guessed_word(secret_word,letters_guess)}')    
            print(dash)
      elif character in letters_guess:
         if warming_left ==0:
            guess_left -=1
            print(f"Oops! You've already guessed that letter.You have no warnings left so you lose one guess:{get_guessed_word(secret_word,letters_guess)}")
            print(dash)
         else:
            warming_left -=1
            print(f"Oops! You've already guessed that letter. You have {warming_left} warnings left:{get_guessed_word(secret_word,letters_guess)}")
            print(dash)
      else:
         letters_guess.append(character)
         if character in secret_word:
            print(f"Good guess:{get_guessed_word(secret_word,letters_guess)}")
            print(dash)
         elif character in ['u','e','o','a','i'] and character not in secret_word:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guess)}")
            print(dash)
            guess_left-=2
         else: 
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guess)}")
            print(dash)
            guess_left-=1
   if guess_left == 0:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
      



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def split(word):
   return  [c for c in word]

def match_with_gaps(my_word, other_word):
   '''
   my_word: string with _ characters, current guess of secret word
   other_word: string, regular English word
   returns: boolean, True if all the actual letters of my_word match the 
      corresponding letters of other_word, or the letter is the special symbol
      _ , and my_word and other_word are of the same length;
      False otherwise: 
   ''' 
   c = 0
   my_word = my_word.replace(' ','')
   my_list = split(my_word)
   other_list = split(other_word)
   if len(my_word) == len(other_word):
      for i in range(len(my_word)):
         if my_word[i] != '_' and my_word[i] != other_word[i]:
            c+=1
         if my_list[i] == '_':
            if other_list[i] in my_list:
               c+=1
      if c==0:
         return True
   return False

                
        
      
    



def show_possible_matches(my_word):
   '''
   my_word: string with _ characters, current guess of secret word
   returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

   ''' 
   for i in wordlist:
      if match_with_gaps(my_word,i):
         print(i, end=' ')     
   print()   




def hangman_with_hints(secret_word):
   '''
   secret_word: string, the secret word to guess.
   
   Starts up an interactive game of Hangman.
   
   * At the start of the game, let the user know how many 
   letters the secret_word contains and how many guesses s/he starts with.
   
   * The user should start with 6 guesses
   
   * Before each round, you should display to the user how many guesses
   s/he has left and the letters that the user has not yet guessed.
   
   * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
   
   * The user should receive feedback immediately after each guess 
   about whether their guess appears in the computer's word.

   * After each guess, you should display to the user the 
   partially guessed word so far.
   
   * If the guess is the symbol *, print out all words in wordlist that
   matches the current guessed word. 
   
   Follows the other limitations detailed in the problem write-up.
   '''
   guess_left = 6
   warming_left = 3
   letters_guess =[]
   dash = '-'*20

   print('Welcome to Hangman')
   print(f"I'm thinking of a word that is {len(secret_word)} letters long")
   print(f'You have {warming_left} warmings left')
   print(dash)
   while(guess_left>0):
      if is_word_guessed(secret_word,letters_guess):
         print('Congratulations, you won!')
         print(f"Your total score for this game:{guess_left*unique(secret_word)}")
         break
      print(f'You have {guess_left} guesses left')
      print(f"Available letters:{get_available_letters(letters_guess)}")
      character = input('Please guess a letter:')
      if len(character) !=1 or str.isalpha(character) == False:  
         if character == '*':
            show_possible_matches(get_guessed_word(secret_word,letters_guess))
         else:
            if warming_left == 0:
               guess_left -=1
               print(f'Oops! That is not a valid letter.You have no warnings left so you lose one guess')
               print(dash)
            else:
               warming_left -=1
               print(f'Oops! That is not a valid letter. You have {warming_left} warnings left:{get_guessed_word(secret_word,letters_guess)}')    
               print(dash)
      elif character in letters_guess:
         if warming_left ==0:
            guess_left -=1
            print(f"Oops! You've already guessed that letter.You have no warnings left so you lose one guess:{get_guessed_word(secret_word,letters_guess)}")
            print(dash)
         else:
            warming_left -=1
            print(f"Oops! You've already guessed that letter. You have {warming_left} warnings left:{get_guessed_word(secret_word,letters_guess)}")
            print(dash)
      else:
         letters_guess.append(character)
         if character in secret_word:
            print(f"Good guess:{get_guessed_word(secret_word,letters_guess)}")
            print(dash)
         elif character in ['u','e','o','a','i'] and character not in secret_word:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guess)}")
            print(dash)
            guess_left-=2
         else: 
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guess)}")
            print(dash)
            guess_left-=1

   if guess_left == 0:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
      
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    # To test part 2, comment out the  line above and
    # uncomment the following two lines.
   # secret_word = choose_word(wordlist)
   # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
   secret_word = choose_word(wordlist)
   hangman_with_hints(secret_word)
print("--- %s seconds ---" % (time.time() - start_time))
