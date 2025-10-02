import pytest
from src.task_bug import add_task
from src.task_bug import mark_task_completed


def test_add_regular_task():
    task_list = []
    add_task(task_list, "Buy milk")
    assert task_list == [("Buy milk", False)]


def test_add_task_with_whitespace():
    task_list = []
    add_task(task_list, "   Learn Python   ")
    assert task_list == [("Learn Python", False)]


def test_add_empty_task():
    task_list = []
    add_task(task_list, "   ")
    assert task_list == []


def test_mark_valid_index():
    task_list = [("Walk dog", False), ("Feed cat", False)]
    mark_task_completed(task_list, 1)
    assert task_list == [("Walk dog", False), ("Feed cat", True)]

def test_mark_first_task():
    task_list = [("Clean room", False)]
    mark_task_completed(task_list, 0)
    assert task_list == [("Clean room", True)]

def test_invalid_index():
    task_list = [("Call mom", False)]
    mark_task_completed(task_list, 5)
    assert task_list == [("Call mom", False)]