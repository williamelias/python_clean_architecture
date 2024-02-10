import pytest
from clean_project.entities import item
from entities import priority, exceptions


@pytest.fixture
def low_task_content():
    yield {
        "title": "tarefa",
        "description": "tarefa desc",
        "priority": priority.Priority.LOW,
    }


@pytest.fixture
def low_task_item(low_task_content):
    yield item.Item(**low_task_content)


def test_title_must_return_exception_when_less_than_3_letters(low_task_content):
    with pytest.raises(
        expected_exception=(
            exceptions.item_exceptions.TitleWithInvalidSizeException
        )
    ):
        low_task_content["title"] = "a"
        item.Item(**low_task_content)


def test_content_of_item(low_task_item, low_task_content):

    assert low_task_content["title"] == low_task_item.get_title()
    assert low_task_content["description"] == (low_task_item.get_description())
    assert low_task_content["priority"] == low_task_item.get_priority()
    assert low_task_item.get_id() is not None


@pytest.mark.parametrize(
    "other_priority",
    [
        priority.Priority.LOW,
        priority.Priority.MIDDLE,
        priority.Priority.HIGHEST,
    ],
)
def test_priority_between_two_itens_is_lt(other_priority, low_task_item):

    afazeres = low_task_item

    estudos = item.Item(
        title="Estudos", description="qualquer coisa", priority=other_priority
    )

    result = afazeres > estudos

    assert result is False


@pytest.mark.parametrize(
    "other_priority",
    [priority.Priority.HIGHEST, priority.Priority.MIDDLE],
)
def test_priority_between_two_itens_is_gt(other_priority, low_task_item):

    afazeres = low_task_item

    estudos = item.Item(
        title="Estudos", description="qualquer coisa", priority=other_priority
    )

    result = estudos > afazeres

    assert result is True
