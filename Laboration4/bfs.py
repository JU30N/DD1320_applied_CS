from bintreeFile_lab4 import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()#svenska tre bokstäver ord 
gamla = Bintree()#besökta ställen 

#with open("C:/Users/joong/Desktop/DD1320/DD1320_applied_CS/Laboration4/word3.txt", "r", encoding="utf-8") as svenskfil:
with open("/Users/ju30n/DD1320_applied_CS/Laboration4/word3.txt", "r", encoding="utf-8") as svenskfil:
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

#byta ord -> kolla om den finns i svenska och inte besökt -> hittat?
#                                                           -> lägg till ordet i kön för att leta vidare från det ordet vi har hittat
# ex leta från 1 till 6
#.      1
#   2           3       5   6
#       4
#börja 1 -> gå till 2 och lägg till 2 i kön och 3 -> från 2 hittat 4 lägg till i kön -> nästa i kön 3 hittat 4 5 lägg till i kö men 4 redan i besökt så lägg inte till i kön
#besök nästa i kön 4 -> inget -> 5 hittar 6 lägg till i kön -> hittat 6!
#
#kön[1] -> [2,3] -> [3] -> [3,4]-> [4,5]-> [5]-> [6]
#besökt[1]-> [1,2]->[1,2,3]-> [1,2,3,4]->[1,2,3,4,5]

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
                gamla.put(new_word)#lägg till att vi har besökt detta ord 

                # if new_word == end_word:#hittat
                #     return True

                q.enqueue(new_word)#kolla denna bit och söker senare vidare [gul,jul,kul]

            if new_word == end_word:#hittat
                return True

        start_word_list[i] = original_char

#kolla en bokstav i taget i ett tre ord -> om ordet finns i svenska och inte i besökta så printa den och lägg till i besökt och lägger till i kön för att leta
# 

def main():
    
    #start_word = input("Start ord: ")
    starting_word = "sov"
    #ending_word = input("Slut ord: ")
    end_wording = "soa"
    q = LinkedQ()
    q.enqueue(starting_word)
    gamla.put(starting_word)
    #makechildren(start_word)
    while not q.isEmpty():
        word = q.dequeue()#ful
        #gamla.put(word)
        foundword = makechildren(word, end_wording, q) #ställen den har varit på och första som finns i listan
        if foundword:#kolla om hittat ordet
            break

    if foundword == None:
        print("Ingen väg hittades")
    else:
        print(f"Det hittades lösning mellan {starting_word} och {end_wording}")

main()