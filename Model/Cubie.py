from enum import Enum
from dataclasses import dataclass
from typing import Dict, Tuple, List
from Model.Direction import Direction
from Model.Color import Color


@dataclass
class Cubie:
    position: Tuple[int, int, int]
    stickers: Dict[Direction, Color]

    def rotate(self, axis: str, cw: bool):
        from Model.Direction import Direction

        dir_to_vec = {
            Direction.UP: (0, 1, 0),
            Direction.DOWN: (0, -1, 0),
            Direction.RIGHT: (1, 0, 0),
            Direction.LEFT: (-1, 0, 0),
            Direction.FRONT: (0, 0, 1),
            Direction.BACK: (0, 0, -1),
        }

        def rotate_vec(v):
            x, y, z = v
            if axis == "x":
                return (x, -z, y) if cw else (x, z, -y)
            if axis == "y":
                return (z, y, -x) if cw else (-z, y, x)
            if axis == "z":
                return (-y, x, z) if cw else (y, -x, z)
            return v

        new_stickers = {}
        for d, col in self.stickers.items():
            vec = dir_to_vec[d]
            new_vec = rotate_vec(vec)
            # 找回对应的 Direction
            for dir_enum, vv in dir_to_vec.items():
                if vv == new_vec:
                    new_stickers[dir_enum] = col
                    break

        self.stickers = new_stickers
