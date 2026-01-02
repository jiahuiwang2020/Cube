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
        self.COLOR_MAP = {
            Color.W: "white",
            Color.Y: "yellow",
            Color.R: "red",
            Color.O: "orange",
            Color.B: "blue",
            Color.G: "green",
        }
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

    def apply_move(self, move: Move, clockwise: bool = True):
        from CubeRotator import CubeRotator

        CubeRotator.execute(self, move, clockwise)

    def is_solved(self) -> bool:
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

    def draw_square(self, ax, vertices, color):
        poly = Poly3DCollection([vertices])
        poly.set_facecolor(color)
        poly.set_edgecolor("black")
        ax.add_collection3d(poly)

    def sticker_vertices(self, x, y, z, direction, size=0.9):
        s = size / 2
        o = 0.5

        if direction == Direction.UP:
            return [
                (x - s, y + o, z - s),
                (x + s, y + o, z - s),
                (x + s, y + o, z + s),
                (x - s, y + o, z + s),
            ]
        if direction == Direction.DOWN:
            return [
                (x - s, y - o, z - s),
                (x + s, y - o, z - s),
                (x + s, y - o, z + s),
                (x - s, y - o, z + s),
            ]
        if direction == Direction.FRONT:
            return [
                (x - s, y - s, z + o),
                (x + s, y - s, z + o),
                (x + s, y + s, z + o),
                (x - s, y + s, z + o),
            ]
        if direction == Direction.BACK:
            return [
                (x - s, y - s, z - o),
                (x + s, y - s, z - o),
                (x + s, y + s, z - o),
                (x - s, y + s, z - o),
            ]
        if direction == Direction.RIGHT:
            return [
                (x + o, y - s, z - s),
                (x + o, y + s, z - s),
                (x + o, y + s, z + s),
                (x + o, y - s, z + s),
            ]
        if direction == Direction.LEFT:
            return [
                (x - o, y - s, z - s),
                (x - o, y + s, z - s),
                (x - o, y + s, z + s),
                (x - o, y - s, z + s),
            ]

    def visualize_3d(self):
        print("Visualizing cube in 3D...")
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection="3d")

        for cubie in self.cubies:
            x, y, z = cubie.position

            for d, color in cubie.stickers.items():
                verts = self.sticker_vertices(x, y, z, d)
                self.draw_square(ax, verts, self.COLOR_MAP[color])

        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])

        ax.set_box_aspect([1, 1, 1])
        ax.axis("off")

        plt.show()
