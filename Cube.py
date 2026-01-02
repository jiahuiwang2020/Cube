from typing import List
from Model.Direction import Direction
from Model.Color import Color
from Model.Cubie import Cubie
from Model.Move import Move
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Cube:
    def __init__(self):
        print("Initializing Cube...")
        self.cubies: List[Cubie] = []
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

    def apply_move(self, move: Move, clockwise: bool = True):
        """Configure the cube by applying a move."""
        from CubeRotator import CubeRotator

        CubeRotator.execute(self, move, clockwise)

    def is_solved(self) -> bool:
        """Check if the cube is in a solved state."""
        is_solved = True
        faces = {
            Direction.UP: lambda p: p[1] == 1,
            Direction.DOWN: lambda p: p[1] == -1,
            Direction.LEFT: lambda p: p[0] == -1,
            Direction.RIGHT: lambda p: p[0] == 1,
            Direction.FRONT: lambda p: p[2] == 1,
            Direction.BACK: lambda p: p[2] == -1,
        }

        for face, selector in faces.items():
            colors = []
            for c in self.cubies:
                if selector(c.position) and face in c.stickers:
                    colors.append(c.stickers[face])

            if len(colors) != 9:
                is_solved = False
                break

            if len(set(colors)) != 1:
                is_solved = False
                break

        return is_solved

    def scramble(self):
        scramble_count = 5

        for _ in range(scramble_count):
            from random import choice, random

            move = choice(list(Move))
            clockwise = random() < 0.5
            self.apply_move(move, clockwise)
