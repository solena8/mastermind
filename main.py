from Mastermind.set import Set
from game import Game


mastermind_game_1 = Game
mastermind_game_1.compare_sets()

game1 = Game(input_coder=Set("Blue", "Green"))
game1.run_baby()