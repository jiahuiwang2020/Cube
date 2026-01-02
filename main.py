from Cube.Model.Cube import Cube
from Cube.Model.Move import Move

cube = Cube()

cube.apply_move(Move("R"))
cube.apply_move(Move("U", clockwise=False))
cube.apply_move(Move("F"))
