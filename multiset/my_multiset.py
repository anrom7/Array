from multiset.myarray import MyArray

class Multiset:
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        """
        self.data = MyArray(100)
        self.firstempty = 0

    def empty(self):
        """
        Checks emptiness of Multiset.

        :return: True if Multiset is empty and False otherwise.
        """
        for index in range(self.firstempty):
            if self.data[index] != None:
                return False
        return True

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        
        :param value: the value to be check.  
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        for index in range(self.firstempty):
            if self.data[index] == value:
                return True
        return False

    def add(self, value):
        """
        Adds the value to multiset.
        
        :param value: the value to be added..
        """
        self.data[self.firstempty] = value
        self.firstempty = self.firstempty + 1

    def delete(self, value):
        """
        Deletes value from multiset.

        :param value: value firs occurrence of which should be deleted.
        """
        position = -1
        current = 0
        while position == -1 and current < self.firstempty:
            if self.data[current] == value:
                position = current
            else:
                current = current + 1
        if current < self.firstempty:
            for updated in range(position, self.firstempty):
                self.data[updated] = self.data[updated + 1]
            self.data[self.firstempty] = None
            self.firstempty = self.firstempty - 1
