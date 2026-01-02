from Cube.Model.CubeRotator import CubeRotator
from typing import List
from Cube.Model.Direction import Direction
from Cube.Model.Color import Color
from Cube.Model.Cubie import Cubie
from Cube.Model.Move import Move


class Cube:
    def __init__(self):
        self.cubies: List[Cubie] = []
        self._init_solved()

    def _init_solved(self):
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    if (x, y, z) == (0, 0, 0):
                        continue

                    stickers = {}
                    if x == 1:
                        stickers[Direction.RIGHT] = Color.R
                    if x == -1:
                        stickers[Direction.LEFT] = Color.O
                    if y == 1:
                        stickers[Direction.UP] = Color.W
                    if y == -1:
                        stickers[Direction.DOWN] = Color.Y
                    if z == 1:
                        stickers[Direction.FRONT] = Color.G
                    if z == -1:
                        stickers[Direction.BACK] = Color.B

                    self.cubies.append(Cubie((x, y, z), stickers))

    def apply_move(self, move: Move):
        CubeRotator.execute(self, move)
