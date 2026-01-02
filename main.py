from Cube import Cube
from Model.Move import Move

cube = Cube()

try_count = 1000000

for _ in range(try_count):
    from random import choice, random

    move = choice(list(Move))
    clockwise = random() < 0.5
    cube.apply_move(move, clockwise)

    if cube.is_solved():
        print(f"Solved the cube in {_ + 1} moves!")
        break

cube.visualize_3d()
