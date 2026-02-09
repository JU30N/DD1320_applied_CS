
from bintreeFile_lab5 import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()#svenska tre bokstäver ord 
gamla = Bintree()#besökta ställen 

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

class SolutionFound(Exception):
    pass

#with open("C:/Users/joong/Desktop/DD1320/DD1320_applied_CS/Laboration4/word3.txt", "r", encoding="utf-8") as svenskfil:
with open("/Users/ju30n/DD1320_applied_CS/Laboration4/word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        #print(ordet)
        if ordet in svenska:
            #print(ordet, end = " ") 
            continue
        else:
            svenska.put(ordet) 

def writechain(node):#newnode => word = son och parent = sov
                # node => word = sov och parent = none
                # print(word = sov)
                     #print(word = son)
    if node.parent is not None:
        writechain(node.parent)#
    print(node.word)

def makechildren(start_node, end_word, q):#sov, blå, tom
    
    alfabeth = "abcdefghijklmnopqrstuvwxyzåäö"
    start_node_word = start_node.word#start_node_word = rootnode.word == sov
    start_word_list = list(start_node_word)
    #print(start_node_word)
    #print(start_word_list)

    for i in range(len(start_word_list)):
        original_char = start_word_list[i]

        for letter in alfabeth:
            
            if letter == original_char:
                continue

            start_word_list[i] = letter
            new_word = "".join(start_word_list)

            if (new_word in svenska) and (new_word not in gamla):
                
                gamla.put(new_word)

                new_node = ParentNode(new_word, start_node)# newnode => word = son och parent = sov

                if new_word == end_word:
                    writechain(new_node)#newnode => word = son och parent = sov
                    raise SolutionFound

                q.enqueue(new_node)

        start_word_list[i] = original_char

#kolla en bokstav i taget i ett tre ord -> om ordet finns i svenska och inte i besökta så printa den och lägg till i besökt och lägger till i kön för att leta
# 


def main():
    #start_word = input("Start ord: ")
    starting_word = "sov"
    #ending_word = input("Slut ord: ")
    end_wording = "får"
    q = LinkedQ()
    
    root = ParentNode(starting_word)# Parent node utan parent men har ett word = sov
    q.enqueue(root)#lägg till denna i queue

    gamla.put(starting_word)#besökt
    #makechildren(start_word)
    try:
        while not q.isEmpty():
            current_node = q.dequeue()#sov
            makechildren(current_node, end_wording, q)#sov, blå, tom queue
        
        print("Det finns ingen väg") 

    except SolutionFound:
        print("hittat")

main()