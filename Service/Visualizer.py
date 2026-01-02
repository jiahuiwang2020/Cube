import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from Model.Color import Color
from Model.Direction import Direction


class Visualizer:
    def __init__(self, cube):
        self.cube = cube
        self.COLOR_MAP = {
            Color.W: "white",
            Color.Y: "yellow",
            Color.R: "red",
            Color.O: "orange",
            Color.B: "blue",
            Color.G: "green",
        }

    def draw_square(self, ax, vertices, color):
        poly = Poly3DCollection([vertices])
        poly.set_facecolor(color)
        poly.set_edgecolor("black")
        ax.add_collection3d(poly)

    def sticker_vertices(self, x, y, z, direction, size=0.9):
        """Method to get the vertices of a sticker on a cubie."""
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

        for cubie in self.cube.cubies:
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
