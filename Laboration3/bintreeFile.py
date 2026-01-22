



def finns(node, value):# True om value finns i trädet, False annars
    if node == None:#finns fler ställen att leta
        return False
    
    if node.data == value:#hittat
        return True

    elif value < node.data:#kolla vänster
        return finns(node.left, value)
    else:#kolla höger
        return finns(node.right, value)


def skriv(node):# Skriver ut trädet i inorder vänster till höger
    if node != None:#hitta där det är en leaf
        #gå vänster kolla vänster, om vänster är klar skriv ut data och 
        #gå höger när det är klar gå tillbaka
        skriv(node.left)
        print(node.data)
        skriv(node.right)

def putta(node, value):#value 1) kolla om den finns eller ej 2) kolla vart man ska lägga in den
    if node == None:
        return Node(value, None, None)
    
    if value < node.data:#om mindre sätt till vänster
        node.left = Node(value, None, None)
    
    elif value > node.data:
        node.right = Node(value, None, None)
    
    return node



class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left 
        self.right = right

    def __str__(self):
        return str(self.data)
    
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def get_data(self):
        return self.data

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root , newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        print(self.root)
        skriv(self.root)
        print("\n")
