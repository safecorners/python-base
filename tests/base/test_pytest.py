import pytest

from base.pytest import add, substract


def test_add() -> None:
    assert add(1, 2) == 3


def test_substract() -> None:
    assert substract(2, 1) == 1
