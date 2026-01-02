from Cube import Cube
from Model.Move import Move
from Service.Visualizer import Visualizer
from Service import RandomSolver


cube = Cube()

## Scramble the cube
cube.scramble()

## Try to solve the cube with different solvers
random_solver_result = RandomSolver.Solve(cube, 100)

visualizer = Visualizer(cube)
visualizer.visualize_3d()
