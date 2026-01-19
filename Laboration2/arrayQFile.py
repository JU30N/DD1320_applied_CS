from array import array
class ArrayQ():
    def __init__(self):#man måste välja om det vad array ska innehålla vilket innebär en nackdel
        self._items = array("I")
        
    def enqueue(self, item):#lägger till längst bak i listan
        self._items.append(item)

    def dequeue(self):#pop första item
        return self._items.pop(0)
    
    def get_size(self):
        return len(self._items)
    
    def get_items(self):
        result = ""
        for i in self._items:
            result += str(i) + " "
        return result
