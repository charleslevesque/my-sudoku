import copy
from dataclasses import dataclass
from enum import Enum
from typing import Any, Self


@dataclass(frozen=True, slots=True)
class PencilMark:
    class Position(Enum):
        TOP_LEFT = 1
        TOP_RIGHT = 2
        BOTTOM_LEFT = 3
        BOTTOM_RIGHT = 4

    value: int
    position: Position = Position.TOP_LEFT

    def __hash__(self) -> int:
        return hash(self.value)


class Square:
    def __init__(self, value: int | None = None):
        self.value = value
        self._pencil_marks: set[PencilMark] = set()

    @property
    def pencil_marks(self) -> set[PencilMark]:
        return self._pencil_marks.copy()

    def add_pencil_mark(self, pencil_mark: PencilMark):
        self._pencil_marks.add(pencil_mark)

    def remove_pencil_mark(self, pencil_mark: PencilMark):
        self._pencil_marks.discard(pencil_mark)

    def clear_pencil_marks(self):
        self._pencil_marks.clear()

    def __add__(self, other: Any) -> Self:
        match other:
            case PencilMark():
                self_copy = copy.deepcopy(self)
                self_copy.add_pencil_mark(other)
                return self_copy
            case _:
                msg = f"Unsupported type for addition: {type(other)}"
                raise TypeError(msg)

        return self

    def __sub__(self, other: Any) -> Self:
        match other:
            case PencilMark():
                self_copy = copy.deepcopy(self)
                self_copy.remove_pencil_mark(other)
                return self_copy
            case _:
                msg = f"Unsupported type for subtraction: {type(other)}"
                raise TypeError(msg)

        return self

    def __iadd__(self, other: Any) -> Self:
        match other:
            case PencilMark():
                self.add_pencil_mark(other)
            case _:
                msg = f"Unsupported type for addition: {type(other)}"
                raise TypeError(msg)

        return self

    def __isub__(self, other: Any) -> Self:
        match other:
            case PencilMark():
                self.remove_pencil_mark(other)
            case _:
                msg = f"Unsupported type for subtraction: {type(other)}"
                raise TypeError(msg)

        return self

    def __str__(self) -> str:
        return f"Square(value={self.value}, pencil_marks={self._pencil_marks})"

    def __repr__(self) -> str:
        return self.__str__()
