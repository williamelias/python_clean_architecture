import pytest
from clean_project.entities import item
from entities import todo_list, priority, owner
from clean_project.entities.exceptions import tem_exceptions


@pytest.fixture
def owner_instance():
    yield owner.Owner(name="tester")


@pytest.fixture
def empty_todo_list(owner_instance):
    yield todo_list.TodoList(owner=owner_instance)


@pytest.fixture
def priorized_items():
    first_item = item.Item(
        title="first", description="first", priority=priority.Priority.LOW
    )
    second_item = item.Item(
        title="second", description="second", priority=priority.Priority.MIDDLE
    )
    third_item = item.Item(
        title="third", description="third", priority=priority.Priority.HIGHEST
    )
    items = [first_item, second_item, third_item]
    return items


def test_sort_method(empty_todo_list, priorized_items):
    first_item, second_item, third_item = priorized_items
    empty_todo_list.add(item=third_item)
    empty_todo_list.add(item=first_item)
    empty_todo_list.add(item=second_item)
    assert empty_todo_list.items == [first_item, second_item, third_item]


def test_add_with_duplicated_item_should_return_exception(
    empty_todo_list, priorized_items
):
    first_item, second_item, _ = priorized_items
    with pytest.raises(expected_exception=tem_exceptions.DuplicatedItemException):
        empty_todo_list.add(item=first_item)
        empty_todo_list.add(item=first_item)
        empty_todo_list.add(item=second_item)
