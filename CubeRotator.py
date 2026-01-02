from Cube import Cube
from Model.Move import Move


class CubeRotator:

    @staticmethod
    def execute(cube: Cube, move: Move, clockwise: bool):
        axis, layer = CubeRotator._face_to_axis(move.value)
        targets = CubeRotator._select(cube.cubies, axis, layer)

        for cubie in targets:
            cubie.position = CubeRotator._rotate_position(
                cubie.position, axis, clockwise
            )
            cubie.rotate(axis, clockwise)

    @staticmethod
    def _face_to_axis(face: str):
        return {
            "R": ("x", 1),
            "L": ("x", -1),
            "U": ("y", 1),
            "D": ("y", -1),
            "F": ("z", 1),
            "B": ("z", -1),
        }[face]

    @staticmethod
    def _select(cubies, axis, layer):
        idx = {"x": 0, "y": 1, "z": 2}[axis]
        return [c for c in cubies if c.position[idx] == layer]

    @staticmethod
    def _rotate_position(pos, axis, cw):
        x, y, z = pos
        if axis == "x":
            # Rotate in the YZ plane
            return (x, -z, y) if cw else (x, z, -y)
        if axis == "y":
            # Rotate in the XZ plane
            return (z, y, -x) if cw else (-z, y, x)
        if axis == "z":
            # Rotate in the XY plane
            return (-y, x, z) if cw else (y, -x, z)
        return pos
