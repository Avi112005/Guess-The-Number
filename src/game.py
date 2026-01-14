import random

class Game:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.game_over = False

    def start_game(self):
        """Main game loop"""
        print(f"I'm thinking of a number between {self.min_num} and {self.max_num}.\n")
        
        while not self.game_over:
            try:
                guess = int(input(f"Enter your guess ({self.min_num}-{self.max_num}): "))
                
                # Validate input
                if guess < self.min_num or guess > self.max_num:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}.\n")
                    continue
                
                self.attempts += 1
                self.check_guess(guess)
                
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")

    def check_guess(self, guess):
        """Check if guess is correct and provide hints"""
        if guess == self.secret_number:
            self.win_game()
        elif guess < self.secret_number:
            print(f"Too Low! Try a higher number.\n")
        else:
            print(f"Too High! Try a lower number.\n")

    def win_game(self):
        """Handle winning condition"""
        self.game_over = True
        print(f"\n🎉 You got it! The number was {self.secret_number}.")
        print(f"You won in {self.attempts} attempts!")
        self.play_again()

    def play_again(self):
        """Ask if player wants to play again"""
        response = input("\nDo you want to play again? (yes/no): ").lower()
        if response in ['yes', 'y']:
            # Restart game
            self.__init__()
            self.start_game()
        else:
            print("Thanks for playing! Goodbye!")