import uuid
from clean_project.entities.base_interface import EntityI
from clean_project.entities.exceptions import item_exceptions
import enum


class Priority(enum.Enum):
    LOW = 1
    MIDDLE = 2
    HIGHEST = 3


class Item(EntityI):
    def __init__(
        self, title: str, description: str, priority: Priority
    ) -> None:
        self.__description = description
        self.__title = self.set_title(title=title)
        self.__priority = priority
        self.__checked = False
        self.__uuid = uuid.uuid4()

    def get_checked(self):
        return self.__checked

    def set_title(self, title: str):
        if len(title) < 3:
            raise item_exceptions.ItemTitleWithInvalidSizeException()
        return title

    def __str__(self) -> str:
        return self.get_title()

    def get_title(self):
        return self.__title

    def __lt__(self, other_item):
        """Override default '<' with new comparing
        embased in .priority field of objects

        Args:
            other_item (Item): _description_

        Returns:
            bool: if self priority is less than other.priority
        """
        return self.__priority.value < other_item.__priority.value

    def __gt__(self, other_item):
        """Override default '>' with new comparing
        embased in .priority field of objects

        Args:
            other_item (Item): _description_

        Returns:
            bool: if self priority is grethen than other.priority
        """
        return self.__priority.value > other_item.__priority.value

    def check(self):
        self.__checked = True

    def uncheck(self):
        self.__checked = False

    def get_description(self):
        return self.__description

    def update_description(self, new_description: str):
        self.__description = new_description

    def update_priority(self, new_priority: int):
        self.__priority = new_priority

    def get_priority(self):
        return self.__priority

    def get_uuid(self):
        return self.__uuid.__str__()

    def __dict__(self):
        return {
            "uuid": self.get_uuid(),
            "title": self.get_title(),
            "description": self.get_description(),
            "checked": self.get_checked(),
            "priority": self.get_priority(),
        }
