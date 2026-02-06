from bintreeFile_lab4 import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()#svenska tre bokstäver ord 
gamla = Bintree()#besökta ställen 

with open("/Users/ju30n/DD1320_applied_CS/Laboration4/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        #print(ordet)
        if ordet in svenska:
            #print(ordet, end = " ") 
            continue
        else:
            svenska.put(ordet)             # in i sökträdet

#Funktionen makechildren ska systematiskt gå igenom alla sätt att byta ut en bokstav
#i startordet (aöt, böt, ..., söö), kolla att det nya ordet finns i
#ordlistan men inte finns i gamla och i så fall skriva ut det nya ordet på
#skärmen och lägga in det i gamla.

def makechildren(start_word):
    
    alfabeth = "abcdefghijklmnopqrstuvwxyzåäö"
    start_word_list = list(start_word)

    for i in range(len(start_word_list)):#0 börjar med exempelvis söt
        original_char = start_word_list[i]#original_char = s 

        for letter in alfabeth:#a
            
            if letter == original_char:
                continue

            start_word_list[i] = letter#letter = a -> s = a
            new_word = "".join(start_word_list)#join till aöt

            if new_word in svenska and new_word not in gamla:
                print(new_word)
                gamla.put(new_word)
                

        start_word_list[i] = original_char

#kolla en bokstav i taget i ett tre ord -> om ordet finns i svenska och inte i besökta så printa den och lägg till i besökt och lägger till i kön för att leta
# 

def main():
    
    #start_word = input("Start ord: ")
    start_word = "söt"
    #end_word = input("Slut ord: ")
    q = LinkedQ()
    q.enqueue(starting_word)
    gamla.put(starting_word)
    #makechildren(start_word)
    while not q.isEmpty():
        nod = q.dequeue()
        makechildren(nod, q) # Skicka med q så funktionen kan lägga in nya barn

main()