def utskrift1(lista):
    if len(lista) > 0:
        
        utskrift1(lista[1:])
        print(lista[0])
def utskrift2(lista):
    if len(lista) > 0:
        print(lista[0])
        utskrift2(lista[1:])
        

def main():
    lista = [1,2,3,4,5]
    utskrift1(lista)
    utskrift2(lista)


main()