from Model.Direction import Direction
from Model.Color import Color
from Model.Move import Move
import Cube


def Solve(cube: Cube, max_iterations: int = 1000):
    """
    分层复原法迭代版：自动从任意 scramble 状态复原
    """

    print("Starting Layer-by-Layer Solve...")

    def move_edge_to_layer(cubie, target_y=-1):
        x, y, z = cubie.position
        if y == target_y:
            return  # 已经在目标层
        # 简单公式示例：如果在顶层 (y==1) → 底层 (y==-1)
        if y == 1:
            cube.apply_move(Move.F, clockwise=True)
            cube.apply_move(Move.U, clockwise=True)
            cube.apply_move(Move.R, clockwise=True)
        elif y == 0:
            cube.apply_move(Move.R, clockwise=True)
            cube.apply_move(Move.D, clockwise=True)
            cube.apply_move(Move.R, clockwise=False)

    def move_corner_to_layer(cubie, target_y=-1):
        x, y, z = cubie.position
        if y == target_y:
            return
        # 使用 R' D' R D 将角块移到底层
        cube.apply_move(Move.R, clockwise=False)
        cube.apply_move(Move.D, clockwise=False)
        cube.apply_move(Move.R, clockwise=True)
        cube.apply_move(Move.D, clockwise=True)

    def apply_move_to_middle(cubie):
        # 把中层边块放到正确位置
        cube.apply_move(Move.U, clockwise=False)
        cube.apply_move(Move.L, clockwise=False)
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.L, clockwise=True)
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.F, clockwise=True)
        cube.apply_move(Move.U, clockwise=False)
        cube.apply_move(Move.F, clockwise=False)

    def apply_top_layer_moves(cubie):
        # 顶层复原公式
        # 先形成十字
        cube.apply_move(Move.F, clockwise=True)
        cube.apply_move(Move.R, clockwise=True)
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.R, clockwise=False)
        cube.apply_move(Move.U, clockwise=False)
        cube.apply_move(Move.F, clockwise=False)
        # 角块旋转
        cube.apply_move(Move.R, clockwise=True)
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.R, clockwise=False)
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.R, clockwise=True)
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.R, clockwise=False)
        # 边块位置调整
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.R, clockwise=True)
        cube.apply_move(Move.U, clockwise=False)
        cube.apply_move(Move.L, clockwise=False)
        cube.apply_move(Move.U, clockwise=True)
        cube.apply_move(Move.R, clockwise=False)
        cube.apply_move(Move.U, clockwise=False)
        cube.apply_move(Move.L, clockwise=True)

    iteration = 0

    while not cube.is_solved() and iteration < max_iterations:
        iteration += 1

        # -------------------
        # 底层操作
        # -------------------
        for cubie in cube.cubies:
            if len(cubie.stickers) == 2:  # 边块
                move_edge_to_layer(cubie)
            elif len(cubie.stickers) == 3:  # 角块
                move_corner_to_layer(cubie)

        # -------------------
        # 中层边块
        # -------------------
        for cubie in cube.cubies:
            if len(cubie.stickers) == 2 and cubie.position[1] == 0:
                apply_move_to_middle(cubie)

        # -------------------
        # 顶层操作
        # -------------------
        for cubie in cube.cubies:
            if cubie.position[1] == 1:
                apply_top_layer_moves(cubie)

    if cube.is_solved():
        print("Cube fully solved!")
    else:
        print("Reached max iterations, cube may not be fully solved.")
