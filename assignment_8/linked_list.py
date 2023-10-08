class Node:
    def __init__(self, value, next=None, previous=None):
        self._value = value
        self._next = next
        self._previous = previous
        
class LinkedList:
    def __init__(self, *args):
        self._first = None
        self.append(args)

    def _append(self, value):
        if self._first is None:
            self._first = Node(value)
        else:
            n = self._first
            while n._next:
                n = n._next
            n._next = Node(value, previous=n)

    def append(self, iterable):
        for value in iterable:
            self._append(value)

    def __iter__(self):
        self._current = self._first
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = self._current._value
        self._current = self._current._next
        return value

    def __contains__(self, value):
        current = self._first
        while current:
            if current._value == value:
                return True
            current = current._next
        return False

    def count(self, value):
        count = 0
        current = self._first
        while current:
            if current._value == value:
                count += 1
            current = current._next
        return count

    def __bool__(self):
        return self._first is not None

    def _len_(self):
        c = 0
        n = self._first
        while n:
            c += 1
            n = n._next
        return c

    def __locate(self, index):
        if index >= len(self):
            raise IndexError(f'Invalid Index: {index}')
        n = self._first
        for i in range(index):
            n = n._next
        return n

    def _getitem_(self, index):
        n = self.__locate(index)
        return n._value

    def _setitem_(self, index, value):
        n = self.__locate(index)
        n._value = value

    def insert(self, index, value):
        y = self.__locate(index)
        x = y._previous
        new_node = Node(value, previous=x, next=y)
        if x:
            x._next = new_node
        else:
            self._first = new_node
        y._previous = new_node

    def remove(self, index):
        n = self.__locate(index)
        x = n._previous
        y = n._next
        if x:
            x._next = y
        else:
            self._first = y
        if y:
            y._previous = x
        return n._value

    def _str_(self):
        if self._first is None:
            return "LinkedList(empty)"
        result = "LinkedList(\t"
        n = self._first
        while n:
            result += f'{n._value}\t'
            n = n._next
        result += ")"
        return result
