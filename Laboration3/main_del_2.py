
from bintreeFile import Bintree
svenska = Bintree()

with open("/Users/ju30n/DD1320_applied_CS/Laboration4/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        #print(ordet)
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
#print(svenska.write())
print("\n")