class Owner:
    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self) -> str:
        return self.get_name()