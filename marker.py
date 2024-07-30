from dataclasses import dataclass
from enum import Enum

@dataclass
class Marker(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5
    BLACK = 6


    def check_match(self, list):
        if self.Marker in list:
            return True
