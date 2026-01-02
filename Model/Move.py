from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Move(Enum):
    R = "R"
    L = "L"
    U = "U"
    D = "D"
    F = "F"
    B = "B"
