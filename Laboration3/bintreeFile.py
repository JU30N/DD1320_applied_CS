



def finns(self):
        pass

def skriv(self):
    pass 

def putta(self):
    pass

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
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

