from molgrafik import Molgrafik

from linkedQ_v2 import LinkedQ

class Ruta:
    def __init__(self, atom = "()", num = 1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

class Syntaxfel(Exception):
    pass

def read_big_letter(i):
    if i.isEmpty() or not i.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav")
    return i.dequeue()

def read_small_letter(i):
    if not i.isEmpty() and i.peek().islower():
        return i.dequeue()
    return ""

def read_atom(i):
    atom = read_big_letter(i)
    atom += read_small_letter(i)
    return atom

def read_num(i):
    if i.isEmpty() or not i.peek().isdigit():
        raise Syntaxfel("Saknad siffra vid radslutet")
    
    if i.peek() == "0":
        i.dequeue()
        raise Syntaxfel("För litet tal vid radslutet")
    
    num_string = ""
    while not i.isEmpty() and i.peek().isdigit():
        num_string += i.dequeue()

    total_number_sum = int(num_string)
    if total_number_sum < 2:
        raise Syntaxfel("För litet tal vid radslutet")
    
    return total_number_sum

def read_group(i):
    ruta = Ruta()

    if i.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    
    if i.peek() == "(":
        i.dequeue()
        ruta.down = read_mol(i)

        if i.isEmpty() or i.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet")
        i.dequeue()

        if i.isEmpty() or not i.peek().isdigit():
            raise Syntaxfel("Saknad siffra vid radslutet")
        
        ruta.num = read_num(i)

    else:
        ruta.atom = read_atom(i)
        if not i.isEmpty() and i.peek().isdigit():
            ruta.num = read_num(i)

    return ruta


def read_mol(i):
    mol = read_group(i)
    if not i.isEmpty() and i.peek() != ")":
        mol.next = read_mol(i)
    return mol


def read_formel(i):
    mol = read_mol(i)
    if not i.isEmpty():
        raise Syntaxfel("Felaktig gruppstart")
    return mol

def check_syntax(mol):
    i = LinkedQ()
    for chr in mol:
        i.enqueue(chr)
    
    try:
        mol = read_formel(i)
        return mol, "Formeln är sytaktiskt korrekt"
    except Syntaxfel as e:
        rest_str = ""
        while not i.isEmpty():
            rest_str += i.dequeue()
        if rest_str != "":
            return None, f"{str(e)} vid radslutet {rest_str}"
        else:
            return None, f"{str(e)}"



def main():
    mg = Molgrafik()
    while True:
        try:
            line = input()
            if line =="#":
                break

            if line != "":
                mol, resultat = check_syntax(line)
                print(resultat)

                if mol != "":
                    mg.show(mol)
        except EOFError:
            break


main()