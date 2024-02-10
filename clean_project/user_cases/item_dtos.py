from dataclasses import dataclass
from entities.priority import Priority


@dataclass
class CreateItemInputDTO:
    title: str
    description: str
    priority: Priority
