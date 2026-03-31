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
        self.__first = None
        self.__last = None

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

        if self.__first is None:
            self.__first = new_node
            self.__last = new_node

        else:
            self.__last.next = new_node
            self.__last = new_node

        

    def dequeue(self):#ta bort första item i listan

        #dequeue()
        #1 = self.first.getvalue <- (D=1 N=node2 )
        #node2 = (D=2 N=none)
        #nya första = nästa av gamla första så 
        #self.first -> (D=1 N=node2)
        #self.first -> (node2)->(D=2 N = node3)
        if self.__first is None:
            return None
        else:
            data_return = self.__first.get_value()
            self.__first = self.__first.next
        return data_return
    
    
    def isEmpty(self):
        if self.__first is None:
            return True
        else:
            return False

    def peek(self):
        if self.__first is None:
            return None
        return self.__first.get_value()