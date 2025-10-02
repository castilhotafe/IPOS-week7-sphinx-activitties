import pytest
from src.task_bug import add_task
from src.task_bug import mark_task_completed
from src.task_bug import delete_task
from src.task_bug import sort_tasks
from src.task_bug import binary_search

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


def test_delete_valid_index():
    tasks = [("Study", False), ("Exercise", False), ("Read", False)]
    tasks_copy = tasks.copy()
    delete_task(tasks_copy, 1)
    assert tasks_copy == [("Study", False), ("Read", False)]

def test_delete_invalid_index():
    tasks = [("Study", False), ("Read", False)]
    delete_task(tasks, 5)
    assert tasks == [("Study", False), ("Read", False)]


def test_sort_tasks():
    tasks = [("Walk dog", False), ("Do homework", True), ("Clean room", False)]
    tasks_copy = tasks.copy()
    sort_tasks(tasks_copy)
    assert tasks_copy == [("Clean room", False), ("Do homework", True), ("Walk dog", False)]


def test_sort_tasks_empty_list():
    empty = []
    sort_tasks(empty)
    assert empty == []


def test_binary_search_found_middle():
    tasks = [("Clean room", False), ("Do homework", True), ("Walk dog", False)]
    message = binary_search(tasks, "Do homework")
    assert message == "Task 'Do homework' found at index 1."

def test_binary_search_found_first():
    tasks = [("Clean room", False), ("Do homework", True), ("Walk dog", False)]
    message = binary_search(tasks, "Clean room")
    assert message == "Task 'Clean room' found at index 0."

def test_binary_search_not_found():
    tasks = [("Clean room", False), ("Do homework", True), ("Walk dog", False)]
    message = binary_search(tasks, "Cook dinner")
    assert message == "Task 'Cook dinner' not found."
