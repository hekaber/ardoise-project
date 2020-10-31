from enum import Enum


class MEnum(Enum):

    @classmethod
    def get_choices(cls):
        return [(tag, tag.value) for tag in cls]
