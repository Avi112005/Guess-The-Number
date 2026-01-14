import random
from game import Game

def main():
    print("Welcome to 'Guess the Number'!")
    print("Try to guess the number I'm thinking of between 1 and 100.")
    
    game = Game()
    game.start_game()

if __name__ == "__main__":
    main()