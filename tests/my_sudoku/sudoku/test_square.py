import pytest

from my_sudoku.sudoku.square import PencilMark, Square


@pytest.fixture
def empty_square() -> Square:
    return Square()


@pytest.fixture
def filled_square() -> Square:
    return Square(5)


def test_square_initialization(empty_square: Square, filled_square: Square):
    assert empty_square.value is None, "Expected an empty square to have a value of None"
    assert filled_square.value == 5, "Expected a filled square to have the correct value"


def test_pencil_mark_management(empty_square: Square):
    pencil_mark1 = PencilMark(1, PencilMark.Position.TOP_LEFT)
    pencil_mark2 = PencilMark(2, PencilMark.Position.BOTTOM_RIGHT)

    # Test adding pencil marks
    empty_square.add_pencil_mark(pencil_mark1)
    empty_square.add_pencil_mark(pencil_mark2)
    assert pencil_mark1 in empty_square.pencil_marks, "Pencil mark 1 should be in the square"
    assert pencil_mark2 in empty_square.pencil_marks, "Pencil mark 2 should be in the square"

    # Test removing a pencil mark
    empty_square.remove_pencil_mark(pencil_mark1)
    assert pencil_mark1 not in empty_square.pencil_marks, "Pencil mark 1 should have been removed"
    assert pencil_mark2 in empty_square.pencil_marks, "Pencil mark 2 should still be in the square"

    # Test clearing pencil marks
    empty_square.clear_pencil_marks()
    assert len(empty_square.pencil_marks) == 0, "All pencil marks should have been cleared"


def test_square_addition_and_subtraction(empty_square: Square):
    pencil_mark1 = PencilMark(1, PencilMark.Position.TOP_LEFT)
    pencil_mark2 = PencilMark(2, PencilMark.Position.BOTTOM_RIGHT)

    # Test addition
    new_square = empty_square + pencil_mark1
    assert pencil_mark1 in new_square.pencil_marks, "Pencil mark 1 should be in the new square"
    assert pencil_mark1 not in empty_square.pencil_marks, "Pencil mark 1 should not be in the original square"

    # Test subtraction
    new_square = new_square - pencil_mark1
    assert pencil_mark1 not in new_square.pencil_marks, "Pencil mark 1 should have been removed from the new square"
    assert pencil_mark1 not in empty_square.pencil_marks, "Pencil mark 1 should not be in the original square"

    # Test in-place addition
    empty_square += pencil_mark2
    assert pencil_mark2 in empty_square.pencil_marks, (
        "Pencil mark 2 should be in the original square after in-place addition"
    )

    # Test in-place subtraction
    empty_square -= pencil_mark2
    assert pencil_mark2 not in empty_square.pencil_marks, (
        "Pencil mark 2 should have been removed from the original square after in-place subtraction"
    )


def test_invalid_operations(empty_square: Square):
    with pytest.raises(TypeError):
        _ = empty_square + 5  # Invalid type for addition

    with pytest.raises(TypeError):
        _ = empty_square - 5  # Invalid type for subtraction

    with pytest.raises(TypeError):
        empty_square += 5  # Invalid type for in-place addition

    with pytest.raises(TypeError):
        empty_square -= 5  # Invalid type for in-place subtraction
