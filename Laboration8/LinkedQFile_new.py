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

        #privata klass gör att q._first = 2 detta är inte möjligt och man kan ej byta från utsidan
        
    def enqueue(self, item):

        # första enqueue(1) -> self._first = none och newnode = (D= 1 N= None) 
        # ->self.first = newnode med (D= 1 N = None)
        #self.first och self.last -> newnode(D=1, N=None)
        #
        #enqueure(2)
        #
        #newnode = (D=2 N=None)
        #self.last.next = newnode -> (D=1 N=None) blir till (D=1 N=newnode) där newnode är (D=2 N= None)
        #self.last = newnode -> self.last pekar på D=2 N=None 
        #


        new_node = Node(item)

        if self._first is None:
            self._first = new_node
            self._last = new_node

        else:
            self._last.next = new_node
            self._last = new_node

        

    def dequeue(self):#ta bort första item i listan

        #dequeue()
        #1 = self.first.getvalue <- (D=1 N=node2 )
        #node2 = (D=2 N=none)
        #nya första = nästa av gamla första så 
        #self.first -> (D=1 N=node2)
        #self.first -> (node2)->(D=2 N = node3)
        if self._first is None:
            return None
        else:
            data_return = self._first.get_value()
            self._first = self._first.next
        return data_return
    
    def get_size(self):
        size_counter = 0
        current = self._first

        while current is not None:
            size_counter += 1
            current = current.next
        return size_counter

    def peek(self):
        if self._first is None:
            return None
        return self._first.get_value()

    def isEmpty(self):
        if self._first is None:
            return True
        else:
            return False
    


    def get_items(self):
        items_list = []
        current = self._first

        while current is not None:
            items_list.append(current.value)
            current = current.next

        for i in range(0, len(items_list)):
            #print(items_list[i])
            print(items_list[i], end=" ")
        

