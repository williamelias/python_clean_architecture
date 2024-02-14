import pytest
from clean_project.entities.todo_item import Item, Priority
from clean_project.entities import exceptions


@pytest.fixture
def low_task_content():
    yield {
        "title": "tarefa",
        "description": "tarefa desc",
        "priority": Priority.LOW,
    }


@pytest.fixture
def low_task_item(low_task_content):
    yield Item(**low_task_content)


def test_title_must_return_exception_when_less_than_3_letters(low_task_content):
    with pytest.raises(
        expected_exception=(exceptions.item_exceptions.TitleWithInvalidSizeException)
    ):
        low_task_content["title"] = "a"
        Item(**low_task_content)


def test_content_of_item(low_task_item, low_task_content):

    assert low_task_content["title"] == low_task_item.get_title()
    assert low_task_content["description"] == (low_task_item.get_description())
    assert low_task_content["priority"] == low_task_item.get_priority()
    assert low_task_item.get_id() is not None


@pytest.mark.parametrize(
    "other_priority",
    [
        Priority.LOW,
        Priority.MIDDLE,
        Priority.HIGHEST,
    ],
)
def test_priority_between_two_itens_is_lt(other_priority, low_task_item):

    afazeres = low_task_item

    estudos = Item(
        title="Estudos", description="qualquer coisa", priority=other_priority
    )

    result = afazeres > estudos

    assert result is False


@pytest.mark.parametrize(
    "other_priority",
    [Priority.HIGHEST, Priority.MIDDLE],
)
def test_priority_between_two_itens_is_gt(other_priority, low_task_item):

    afazeres = low_task_item

    estudos = Item(
        title="Estudos", description="qualquer coisa", priority=other_priority
    )

    result = estudos > afazeres

    assert result is True
