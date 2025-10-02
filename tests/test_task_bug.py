import pytest
from src.task_bug import add_task

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
