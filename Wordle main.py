from random import randint


class GuessLengthError(Exception):
    """Raised when the guess is not 5 alphabets long"""
    pass

class SpecialCharactersError(Exception):
    """Raised when the guess contains characters other than a-z"""
    pass

class InvalidGuessError(Exception):
    """Raised when the guess is not a valid word.
    I.E. word is not in the possible guess & answers list"""
    pass



with open("wordle-answers-alphabetical.txt", "r") as a:
    #Putting the answers from text file into a list.
    #This list does not contain the possible guesses.
    #ANSWER TXT FILE CREDIT: Medium
    
    answers = a.readlines()
    answer_list = []
    for word in answers:
        answer_list.append(word[:5])



with open("wordle-allowed-guesses.txt", "r") as g:
    #Putting the answers from text file into a list.
    #This list does not contain the possible guesses.
    #ANSWER TXT FILE CREDIT: Medium]
    
    guesses = g.readlines()
    guess_list = []
    for word in guesses:
        guess_list.append(word[:5])



def print_game_rules():
    """function to print welcome message.
    Parameter: None, Return: None, Output: welcome message"""
    
    print("Let's play Wordle!")
    print("You get six guesses")
    print("Game markings:")
    print("\tStar (~) sign: Incorrect alphabet")
    print("\tPlus (+) sign: Correct alphabet, wrong place")
    print("\tEqual (=) sign: Correct alphabet, correct place")



def random_value():
    """function to generate a random value, to get a random word for the game.
    Parameter: None, Return: A string containing answer, Output: None"""
    
    value = randint(0, 2315)
    print(answer_list[value])   #to be erased afterwards

    return answer_list[value]



def compare_word(guess, answer):
    """function to compare user's word with the correct answer
    Parameter: word, Return: None, Output: comparison of the guess"""
    
    boxed_str = ''
    
    for i in range(5):
        if (guess[i] != answer[i]) and (guess[i] in answer):
            boxed_str += f'| + '
        elif guess[i] != answer[i]:
            boxed_str += f'| ~ '
        elif guess[i] == answer[i]:
            boxed_str += f'| = '

    boxed_str += '|'

    print(boxed_str)
    print(f'| {guess[0]} | {guess[1]} | {guess[2]} | {guess[3]} | {guess[4]} |')
    print(boxed_str)



print_game_rules()
ans = random_value()
game = True

for guess_num in range(1, 7):
    while game:
        try:    
            user_word = input(f"Guess #{guess_num}: ")
        
            if len(user_word) != 5:
                raise GuessLengthError
            if user_word.isalpha() == False:
                raise SpecialCharactersError
            if (user_word not in answer_list) and (user_word not in guess_list):
                raise InvalidGuessError

            if user_word == ans:
                game = False
                print("CONGRATS! YOU CORRECTLY GUESSED THE WORD")
            else:
                compare_word(user_word, ans)

            break
        
        except GuessLengthError:
            print("Guess should be 5 letters, try again!\n")
        except SpecialCharactersError:
            print("Guess should only contain a-z alphabets, try again!\n")
        except InvalidGuessError:
            print("Guess is not a valid word, try again!\n")

        if game == False:
            break

if game:
    print("You have run out of guesses :(")
    print(f"The answer was {ans}")
