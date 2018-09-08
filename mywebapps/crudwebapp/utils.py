"""Utils"""
from enum import Enum


class ChoiceEnum(Enum):
    """Enumeration for model."""
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
