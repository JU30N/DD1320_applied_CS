from bintreeFile_lab4 import Bintree
svenska = Bintree()
gamla = Bintree()

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
    
    alfabeth = "abcdefghijklmnopqrstuvwzåäö"
    start_word_list = list(start_word)

    for i in range(len(start_word_list)):
        original_char = start_word_list[i]

        for letter in alfabeth:
            
            if letter == original_char:
                continue
            start_word_list[i] = letter
            new_word = "".join(start_word_list)

            if new_word in svenska and new_word not in gamla:
                print(new_word)
                gamla.put(new_word)
                

        start_word_list[i] = original_char
    


def main():
    #start_word = input("Start ord: ")
    start_word = "söt"
    #end_word = input("Slut ord: ")
    makechildren(start_word)
    

main()