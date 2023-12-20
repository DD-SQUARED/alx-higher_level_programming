#!/usr/bin/python3
"""Define a class square."""
class square:
    """Represent a square."""

    def_init_(self,size=0):
        """Initialize a new Square.
        Args:
        size(int):The size of the square."""

    @property
    def size(self):
        """Get/set the size of the square."""
        return(self._size)

    @size.setter
    def size(self,value):
        if not isinstance(size,int):
            raise TypeError("size is not an integer")
        elif size < 0
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """Return area of square."""
        return(self._size * self._size)

    def my_print(self):
        """Print Square with character #."""
        for i in range(0, self._size):
            [print("#",end="")for j in range(self._size)]
            print("")
        if self._size == 0:
            print("")

