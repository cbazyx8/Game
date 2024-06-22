import random

def welcome_message():
    print("\033[95m\033[1m")  # Set color to bright magenta and bold text
    print("##############################################")
    print("#                                            #")
    print("#         Welcome to Guess the Number!       #")
    print("#                                            #")
    print("##############################################")
    print("#                                            #")
    print("#           Developed by Wahab Khan          #")
    print("#                                            #")
    print("##############################################")
    print("\033[0m")  # Reset color

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    welcome_message()

    print("\033[93mLet's start the game! I'm thinking of a number between 1 and 100.\033[0m")
    
    while True:
        try:
            guess = int(input("\033[94mEnter your guess: \033[0m"))
            attempts += 1

            if guess < number_to_guess:
                print("\033[91mToo low! Try again.\033[0m")
            elif guess > number_to_guess:
                print("\033[91mToo high! Try again.\033[0m")
            else:
                print(f"\033[92mCongratulations! You guessed the number in {attempts} attempts!\033[0m")
                break
        except ValueError:
            print("\033[91mPlease enter a valid number.\033[0m")

if __name__ == "__main__":
    play_game()
