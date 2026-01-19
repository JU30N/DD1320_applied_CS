class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)
    
    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value


class LinkedQ:
    def __init__(self):
        self._first = None
        self._last = None
        
    def enqueue(self):
        pass

    def dequeue(self):
        pass
    
    def get_size(self):
        pass

