import pytest
from src.tac_tac_bug_toe import is_win


def test_win_horizontal():
    board = [['X', 'X', 'X'],
             ['O', ' ', 'O'],
             [' ', ' ', ' ']]
    assert is_win('X', board) is True

def test_win_vertical():
    board = [['O', 'X', ' '],
             ['O', 'X', ' '],
             ['O', ' ', 'X']]
    assert is_win('O', board) is True

def test_win_diagonal_top_left_to_bottom_right():
    board = [['X', 'O', ' '],
             ['O', 'X', ' '],
             [' ', ' ', 'X']]
    assert is_win('X', board) is True

def test_win_diagonal_top_right_to_bottom_left():
    board = [[' ', ' ', 'O'],
             [' ', 'O', 'X'],
             ['O', ' ', 'X']]
    assert is_win('O', board) is True

def test_no_win():
    board = [['X', 'O', 'X'],
             ['O', 'O', 'X'],
             ['X', 'X', 'O']]
    assert is_win('X', board) is False