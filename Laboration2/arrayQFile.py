from array import array
class ArrayQ():
    def __init__(self):
        self._items = array("I")
        
    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)
    
    def get_size(self):
        return len(self._items)
    
    def get_items(self):
        result = ""
        for i in self._items:
            result += str(i) + " "
        return result
