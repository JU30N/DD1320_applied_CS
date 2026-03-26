import unittest
#from LinkedQFile_new import LinkedQ
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
        


class Syntaxfel(Exception):
    pass



def read_letter(q):
    if q.isEmpty() or not q.peek().isupper():#om kön är tom eller inte ABCD
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    q.dequeue()#ta ut ur kön

def read_small_letter(q):
    q.dequeue()#problem om man återanvänder pga dequeue

def read_atom(q):
    read_letter(q)#Måste börja med stor bokstav 
    if not q.isEmpty() and q.peek().islower():#lägg till om efter stora är liten Au
        read_small_letter(q)

def read_mole(q):#börjar alltid med stor 
    read_atom(q)
    if not q.isEmpty():#bör vara tal
        read_num(q)

    if not q.isEmpty():
        if q.peek().isupper() or q.peek() == "(":
            read_mole(q)
        else:
            raise Syntaxfel("Felaktig gruppstart")


def read_num(q):
    c = q.peek()
    
    if c =='0':#får ej böja med 0
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet")
    
    if c.isdigit():#check siffra läs in som str
        num_str = ""
        while not q.isEmpty() and q.peek().isdigit():
            num_str += q.dequeue()#lägg till första i kön till numstr
        if int(num_str) < 2:#för litet?
            raise Syntaxfel("För litet tal vid radslutet")
        


def checking_syntax(mole_str):
    q = LinkedQ()#en chr i taget
    for chr in mole_str:
        q.enqueue(chr)
    
    try:
        read_mole(q)#starna med mole
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:#kolla var felet skedde
        rest = ""
        while not q.isEmpty():
            rest += q.dequeue()#reseten
        if rest:
            return f"{e} {rest}"
        else:
            return str(e)

class TestingMethod(unittest.TestCase):
    def test_atom(self):
        atom = checking_syntax("Na")
        self.assertEqual(atom, "Formeln är syntaktiskt korrekt")

    def test_number(self):
        number = checking_syntax("Na1")
        self.assertIn("För litet tal vid radslutet", number)

    def test_mole(self):
        mole = checking_syntax("Na2H3")
        self.assertEqual(mole, "Formeln är syntaktiskt korrekt")

def main():
    try:#startar
        while True:
            line = input().strip()
            
            if line =="#":
                break

            if line:
                resultat = checking_syntax(line)
                print(resultat)
    except:
        pass

unittest.main()


