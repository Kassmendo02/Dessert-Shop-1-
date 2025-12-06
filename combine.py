# combine.py

from typing import Protocol, runtime_checkable


@runtime_checkable
class Combinable(Protocol):
    """
    A protocol that represents items that can be combined
    (such as Candy and Cookie objects).
    """

    def can_combine(self, other: "Combinable") -> bool:
        """Return True if two items can be combined, otherwise False."""
        ...

    def combine(self, other: "Combinable") -> "Combinable":
        """Combine two items and return the combined result."""
        ...
