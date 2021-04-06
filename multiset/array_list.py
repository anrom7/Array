class MyArray:
    def __init__(self, size):
        """
        Produces a newly constructed empty array.
        :param size: size of array.
        """
        self._items = []
        self._size = size
        for i in range(size):
            self._items.append(None)

    def __str__(self):
        """
        Converts structure to a string.

        :return: converted structure.
        """
        to_return = "("
        for index in range(self._size - 1):
            to_print = str(self[index])
            to_return = to_return + to_print + ","
        to_print = str(self[self._size - 1])
        return to_return + to_print +")"

    def __len__(self):
        """
        Return length of array.
        :return: 
        """
        return self._size
    
    def __getitem__(self, index):
        """
        Gets the data item with given index.
        Requires: 0 <= index < self.size
        
        :param index: index of the item. 
        :return: the data item with given index.
        """
        return self._items[index]

    def __setitem__(self, index, value):
        """
        Sets the data item with given index.
        Requires: 0 <= index < self.size
        
        :param index: index of the item.
        :param value: value of the item.
        """
        self._items[index] = value
