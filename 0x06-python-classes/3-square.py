#!/usr/bin/python3
"""Define a class square."""
class square:
    """Represent a square."""

    def_init_(self,size=0):
        """Initialize a new Square.
        Args:
        size(int):The size of the square."""

        if not isinstance(size,int):
            raise TypeError("size is not an integer")
        elif size < 0
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """Return area of square."""
        return(self._size * self._size)
