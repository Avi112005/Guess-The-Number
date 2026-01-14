import unittest
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_start_game_initializes(self):
        self.game.start_game()
        self.assertIsNotNone(self.game.secret_number)
        self.assertEqual(self.game.attempts, 0)

    def test_check_guess_correct(self):
        self.game.secret_number = 50
        result = self.game.check_guess(50)
        self.assertEqual(result, "Correct! You've guessed the number.")

    def test_check_guess_too_high(self):
        self.game.secret_number = 50
        result = self.game.check_guess(60)
        self.assertEqual(result, "Too high! Try again.")

    def test_check_guess_too_low(self):
        self.game.secret_number = 50
        result = self.game.check_guess(40)
        self.assertEqual(result, "Too low! Try again.")

    def test_provide_hint(self):
        self.game.secret_number = 50
        hint = self.game.provide_hint(45)
        self.assertIn("higher", hint)

if __name__ == '__main__':
    unittest.main()