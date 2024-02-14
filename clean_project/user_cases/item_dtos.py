from dataclasses import dataclass


@dataclass
class CreateItemInputDTO:
    title: str
    description: str
    priority: str
