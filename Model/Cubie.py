from enum import Enum
from dataclasses import dataclass
from typing import Dict, Tuple, List
from Cube.Model.Direction import Direction
from Cube.Model.Color import Color


@dataclass
class Cubie:
    position: Tuple[int, int, int]
    stickers: Dict[Direction, Color]

    def rotate(self, axis: str, clockwise: bool):
        if axis == "x":
            mapping = {
                Direction.UP: Direction.BACK,
                Direction.BACK: Direction.DOWN,
                Direction.DOWN: Direction.FRONT,
                Direction.FRONT: Direction.UP,
            }
        elif axis == "y":
            mapping = {
                Direction.FRONT: Direction.RIGHT,
                Direction.RIGHT: Direction.BACK,
                Direction.BACK: Direction.LEFT,
                Direction.LEFT: Direction.FRONT,
            }
        elif axis == "z":
            mapping = {
                Direction.UP: Direction.RIGHT,
                Direction.RIGHT: Direction.DOWN,
                Direction.DOWN: Direction.LEFT,
                Direction.LEFT: Direction.UP,
            }
        else:
            return

        if not clockwise:
            mapping = {v: k for k, v in mapping.items()}

        new_stickers = {}
        for d, c in self.stickers.items():
            new_stickers[mapping.get(d, d)] = c

        self.stickers = new_stickers
