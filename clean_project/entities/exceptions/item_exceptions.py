class DuplicatedItemException(Exception):
    text = "Item duplicado"


class ItemTitleWithInvalidSizeException(Exception):
    text = "Wrong size of title"
