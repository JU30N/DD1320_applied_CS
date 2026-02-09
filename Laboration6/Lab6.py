import timeit

class Song:
    def __init__(self, trackid, songtime, artistname, title):
        self.trackid = trackid
        self.songtime = songtime
        self.artistname = artistname
        self.title = title

    def __It__(self, other):
        return self.artistname < other.artistname
    
def readfile():
    song_list = []
    with open("C:\\Users\\joong\\Desktop\\DD1320\\DD1320_applied_CS\\Laboration6\\unique_tracks.txt", "r", encoding="utf-8") as file:        
        for line in file:
            part = line.strip().split("<SEP>")
                                #trackid , songtime artistname title
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


#delar tills bara ett element kvar - jämför element mot element och sedan bygg en ny lista -  b c / a d 
#b vs a - a minst lägg till i listan - b vs c 

#i vänster j höger k ? lista 
def mergesort(lista):
    if len(lista) > 1:
        mitten = len(lista) // 2
        vensterHalva = lista[:mitten]
        hogerHalva = lista[mitten:]

        mergesort(vensterHalva)
        mergesort(hogerHalva)

        i = j = k = 0

        while i < len(vensterHalva) and j < len(hogerHalva):
            if vensterHalva[i].artistname < hogerHalva[j].artistname:#jämför först i kön
                lista[k] = vensterHalva[i]#vänster större
                i += 1#gå till nästa artist i vänster lista 
            else:
                lista[k] = hogerHalva[j]#höger större
                j += 1
            k += 1

        while i < len(vensterHalva):#kollar om det finns något kvar 
            lista[k] = vensterHalva[i]
            i += 1
            k += 1

        while j < len(hogerHalva):
            lista[k] = hogerHalva[j]
            j += 1
            k += 1

def main():

    lista = readfile()
    n = len(lista)
    #print("Antal element =", n)

    hash_with_dict = hashSearch(lista)

    sista = lista[n-1]
    testartist = sista.artistname

    # linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 100000)
    # print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    # binartid = timeit.timeit(stmt = lambda: binarySearch(lista, testartist), number = 100000)
    # print("Binärasökningen tog", round(binartid, 4) , "sekunder")

    # hashtid = timeit.timeit(stmt = lambda: hash_with_dict.get(testartist), number = 100000)
    # print("hash tog", round(hashtid, 4) , "sekunder")
    test_storlek = 10000000
    mindre_lista = lista[:test_storlek]
    
    # Skapa en kopia så vi inte förstör ursprungslistan
    sorterings_lista = mindre_lista.copy()
    
    print("Antal element =", test_storlek)

    # NU skickar vi listan till quicksort
    t_quick = timeit.timeit(lambda: quicksort(sorterings_lista), number=1)#normalt nlogn men värsta fall n^2
        
    t_merge = timeit.timeit(lambda: mergesort(sorterings_lista), number=1)#tid alltid på nlogn
    print(f"{round(t_quick, 5)} s | {round(t_merge, 5)} s")



main()
#med tid och det stämmer det eftersom lin > binar > hash i tid
