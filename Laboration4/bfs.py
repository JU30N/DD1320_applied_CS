from bintreeFile_lab4 import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()#svenska tre bokstäver ord 
gamla = Bintree()#besökta ställen 

with open("C:/Users/joong/Desktop/DD1320/DD1320_applied_CS/Laboration4/word3.txt", "r", encoding="utf-8") as svenskfil:
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

def makechildren(start_word, end_word, q):
    
    alfabeth = "abcdefghijklmnopqrstuvwxyzåäö"
    start_word_list = list(start_word)

    for i in range(len(start_word_list)):#0 börjar med exempelvis söt
        original_char = start_word_list[i]#original_char = s 

        for letter in alfabeth:#a
            
            if letter == original_char:
                continue

            start_word_list[i] = letter#letter = a -> s = a
            new_word = "".join(start_word_list)#join till aöt

            if (new_word in svenska) and (new_word not in gamla):#kolla om den finns här eller inte
                #print(new_word)
                gamla.put(new_word)

                if new_word == end_word:#hittat
                    return True

                q.enqueue(new_word)#kolla denna bit och söker senare vidare [gul,jul,kul]

        start_word_list[i] = original_char

#kolla en bokstav i taget i ett tre ord -> om ordet finns i svenska och inte i besökta så printa den och lägg till i besökt och lägger till i kön för att leta
# 

def main():
    
    #start_word = input("Start ord: ")
    starting_word = "ska"
    #ending_word = input("Slut ord: ")
    end_wording = "luv"
    q = LinkedQ()
    q.enqueue(starting_word)
    gamla.put(starting_word)
    #makechildren(start_word)
    while not q.isEmpty():
        word = q.dequeue()#ful
        foundword = makechildren(word, end_wording, q) #ställen den har varit på och första som finns i listan
        if foundword:#om detta är true printa lösningen
            break

    if foundword == None:
        print("Ingen väg hittades")
    else:
        print(f"Det hittades lösning mellan {starting_word} och {end_wording}")

main()