from bintreeFile import Bintree
svenska = Bintree()

with open("c:/Users/joong/Desktop/DD1320/DD1320_applied_CS/Laboration3/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        #print(ordet)
        if ordet in svenska:
            #print(ordet, end = " ") 
            continue
        else:
            svenska.put(ordet)             # in i sökträdet
#print(svenska.write())
#print("\n")

english = Bintree()
with open("c:/Users/joong/Desktop/DD1320/DD1320_applied_CS/Laboration3/engelska.txt", "r", encoding = "utf-8") as engfil:
    for row in engfil:
        words = row.split()
        #print(words)
        for i in words:
            cleaned_word = i.strip('!".,?"')
            #print(cleaned_word)

            if cleaned_word in english:
                continue
            else:
                english.put(cleaned_word)
                if cleaned_word in svenska:
                    print(cleaned_word, end = " ")
