import timeit

class Song:
    def __init__(self, trackid, songtime, artistname, title):
        self.trackid = trackid
        self.songtime = songtime
        self.artistname = artistname
        self.title = title

    def __lt__(self, other):
        return self.artistname < other.artistname
    
def readfile():
    song_list = []
    # with open("/Users/ju30n/DD1320_applied_CS/Laboration6/unique_tracks.txt", "r", encoding="utf-8") as file:
    with open(r"C:\Users\joong\Desktop\DD1320\DD1320_applied_CS\Laboration6\unique_tracks.txt", "r", encoding="utf-8") as file:
        for line in file:
            part = line.strip().split("<SEP>")
                                #trackid , songtime artistname titles
            song_list.append(Song(part[0],part[1],part[2],part[3]))
    return song_list

def linsok(lista, target):
    for item in lista:
        if item.artistname == target:
            return True
    return False

def binarySearch(alist, item):#tagen från boken dock modifierad
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint].artistname == item:
            found = True
        else:
            if item < alist[midpoint].artistname:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

def hashSearch(alist):
    dictionary = {}
    for song in alist:
        #print(song.artistname)
        #print(song)
        dictionary[song.artistname] = song
    return dictionary

#väljer mitten - partitionerar trörre element till höger och mindre till vänster
#
def quicksort(data):#tagen från gemini 
    if len(data) <= 1:
        return data
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    if low < high:
        pivotindex = (low + high) // 2
        # Flytta pivot till kanten
        data[pivotindex], data[high] = data[high], data[pivotindex]  
        
        # Partitionera baserat på artistname
        pivotmid = partitionera(data, low, high, data[high].artistname) 
        
        # Flytta tillbaka pivot
        data[pivotmid], data[high] = data[high], data[pivotmid]       
        
        qsort(data, low, pivotmid - 1)
        qsort(data, pivotmid + 1, high)

def partitionera(data, v, h, pivot_name):
    i = v - 1
    for j in range(v, h):
        # Här jämför vi artistnamnet på låten med pivot-namnet
        if data[j].artistname < pivot_name:#kollar om den är mindre 
            i += 1
            data[i], data[j] = data[j], data[i]#mindre till vänster och större till höger 
    return i + 1    #nästa placerings steg 



def selectionSort(alist):#tagen från boken med ändringar så den passar till mitt program
    for fillslot in range(len(alist)-1, 0, -1):#letar efter största värde
        positionOfMax = 0
        print(positionOfMax)
        for location in range(1, fillslot + 1):#kollar mellan index 1 och fillslot + 1
            if alist[positionOfMax] < alist[location]:#om man hittar något större så byt platserna
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]#här byts platserna

def main():

    n = 100000


    storLista = readfile()
    mindreLista = storLista[0:n]
    #print("Antal element =", n)
    sorterings_lista_q = mindreLista.copy()
    sorterings_lista_s = mindreLista.copy()

    hash_with_dict = hashSearch(mindreLista)

    sista = mindreLista[n-1]
    testartist = sista.artistname
    #print(testartist)

    # linjtid = timeit.timeit(stmt = lambda: linsok(mindreLista, testartist), number = 10000)
    # print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    # binartid = timeit.timeit(stmt = lambda: binarySearch(mindreLista, testartist), number = 10000)
    # print("Binärasökningen tog", round(binartid, 4) , "sekunder")

    # hashtid = timeit.timeit(stmt = lambda: hash_with_dict.get(testartist), number = 10000)
    # print("hash tog", round(hashtid, 4) , "sekunder")
    
    
    #kopia så vi inte förstör ursprungslistan    

    t_quick = timeit.timeit(lambda: quicksort(sorterings_lista_q), number=1)#n log n
    print(t_quick)
    t_select = timeit.timeit(lambda: selectionSort(sorterings_lista_s), number=1)#n^2
    print(t_select)



main()
#med tid och det stämmer det eftersom lin > binar > hash i tid

#   n = 250 000     n = 500 000         n = 1 000 000
#L  8.5             0.48                0.0818
#B  0.013           0.0131              0.0141
#H  0.0004          0.0004              0.0004
#
#   n = 1000        n=10000         n=100000        n=1000000
#q  0.00066         0.00918         0.13436         2.678
#s  0.03181         3.7236          1559.8042015           tog för lång tid mer än 5 min 
#
#

