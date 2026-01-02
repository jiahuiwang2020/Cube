from typing import List
from Cube import Cube
from Model.Move import Move
from random import choice, random


def Solve(cube: Cube, try_count: int) -> Cube:
    for _ in range(try_count):
        move = choice(list(Move))
        clockwise = random() < 0.5
        cube.apply_move(move, clockwise)

    if cube.is_solved():
        print(f"Solved the cube in {_ + 1} moves!")
        return cube
