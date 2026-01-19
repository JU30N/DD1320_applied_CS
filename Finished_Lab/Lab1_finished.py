import math
import os 


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data

class Planets:
    def __init__(self, name, omloppstid, avstand):
        self.name = name
        self.omloppstid = omloppstid
        self.avstand = avstand
        self.mass = ((4 * (math.pi**2) * (self.avstand**3)) / ((6.67 * 10**-11) * (self.omloppstid**2)))

    def __str__(self):
        return str(self.name)

    def get_mass(self):
        return float(self.mass)
    



def main():

    planeterna = None
    
    with open("c:/Users/joong/Desktop/DD1320/DD1320_applied_CS/Laboration1.py/Lab1_files.txt", "r") as file:
        lines = file.readlines()
        #print(lines)
    #print(len(lines))

    for i in range(0, len(lines), 3):
        #print(lines[i].strip("\n"))
        #print(float(lines[i+1].strip("\n")))
        #print(float(lines[i+2].strip("\n")))
        planet = Planets(lines[i].strip("\n"), float(lines[i+1].strip("\n")), float(lines[i+2].strip("\n")))
        #print(planet.get_mass())
        newNode = Node(planet)
        #if planeterna => None + newnode if planeterna => newnode => 
        if planeterna is None:
            planeterna = newNode
        else: 
            current = planeterna
            while current.get_next() is not None:
                current = current.get_next()
            current.next = newNode  

    if planeterna is not None:
        print("Planet           |          Massa")
        current = planeterna
        while current is not None:
            print(current,"    |     ", current.get_data().get_mass(), "kg" )
            #print(current.get_data().get_mass())
            current = current.get_next()
            




if __name__ == "__main__":
    main()