# Class is a binary max heap meant to contain Schedule objects
# Tony Situ 
# 2023-06-13

from Schedule import Schedule

class BinaryMaxHeap:
    def __init__(self, iterable=[]) -> None:
        self._elems = []
        for elem in iterable:
            self._elems.add(elem)
    
    def __str__(self) -> str:
        return "[{}]".format("\n\n".join([repr(course) for course in self._elems]))
    
    def __len__(self) -> int:
        return len(self._elems)
    
    def __iter__(self):
        return iter(self._elems)
    
    def __getitem__(self, index) -> Schedule:
        if len(self._elems) == 0:
            raise IndexError("get from empty heap")
        return self._elems[index]
    
    def add(self, schedule: Schedule) -> None:
        self._elems.append(schedule)
        self._bubble_up(len(self) - 1)
    
    def _bubble_up(self, i: int) -> None:
        p = parent(i)
        while i > 0 and self._elems[i].get_rating() > self._elems[p].get_rating():
            self._elems[i], self._elems[p] = self._elems[p], self._elems[i]
            i = p
            p = parent(i)

def left(i: int) -> int:
    """Return the index of the left child of the node at index i.
    """
    return 2 * i + 1


def right(i: int) -> int:
    """Return the index of the right child of the node at index i.
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """Return the index of the parent of the node at index i."""
    return (i - 1) // 2