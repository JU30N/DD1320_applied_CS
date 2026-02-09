import timeit





def linsok(lista, target):
    for item in lista:
        if item.artist == target:
            return True
    return False


def main():

    lista = filename
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

main()