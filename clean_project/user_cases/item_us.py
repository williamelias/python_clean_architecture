from . import base
from clean_project.entities.todo_item import Item
from clean_project.gateways.item_gw import GenericGateway
from .item_dtos import CreateItemInputDTO


class CreateItemUS(base.UserCaseInterface):
    def __init__(self, gateway: GenericGateway) -> None:
        self.gateway = gateway

    def execute(self, input: CreateItemInputDTO):
        """Execution of Create todo item Use case
        first, create an instance of Item
        after that, call gateway to persist data
        at the end, return fields of created Item

        Args:
            input (CreateItemInputDTO): It is an interface of
            Item creation fields

        Returns:
            dict: fields of Item
        """
        item = Item(**input)
        self.gateway.create(item)
        return {
            "title": item.get_title(),
            "description": item.get_description(),
            "priority": item.get_priority(),
        }
