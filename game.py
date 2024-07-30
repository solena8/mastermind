from dataclasses import dataclass
from set import Set
from clues import Clues


@dataclass
class Game:
    input_coder: Set
    # input_decoder: Set
    # unmatched_coder: Set = Set(None, None, None, None)
    # unmatched_decoder: Set = Set(None, None, None, None)
    # clues = Clues

    # def _init_(self):
    #     self.input_coder =
    #     self.input_decoder =
    #     self.unmatched_coder =
    #     self.unmatched_decoder =
    #     self.clues = Clues()

    def run_baby(self):
        for turn in range(12):
            set = user_give_me_input()
            self.compare_sets(set)

# version avec des listes, comment faire avec des Sets ?:
    def compare_sets(self, input_decode: Set) -> Clues:
        self.clues.good_color_good_place_count = 0
        self.clues.good_color_bad_place_count = 0
        for i in range(len(self.input_codeur)):
            if self.input_codeur[i] == self.input_decodeur[i]:
                self.clues.good_color_good_place_count += 1
            else:
                self.unmatched_codeur.append(self.input_codeur[i])
                self.unmatched_decodeur.append(self.input_decodeur[i])
        for color in self.unmatched_codeur:
            if color in self.unmatched_decodeur:
                self.clues.good_color_bad_place_count += 1
                self.unmatched_decodeur.remove(color)
        clues = Clues()
        self.clues.give_clues()
        return clues


