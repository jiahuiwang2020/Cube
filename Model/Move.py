from dataclasses import dataclass


@dataclass(frozen=True)
class Move:
    face: str  # 'R', 'L', 'U', 'D', 'F', 'B'
    clockwise: bool = True
