import unittest

"<formel>::= <mol> \n"
"<mol>   ::= <group> | <group><mol>"
"<group> ::= <atom> |<atom><num> | (<mol>) <num>"
"<atom>  ::= <LETTER> | <LETTER><letter>"
"<LETTER>::= A | B | C | ... | Z"
"<letter>::= a | b | c | ... | z"
"<num>   ::= 2 | 3 | 4 | ..."





atom_list = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv".split()

class Syntaxerror(Exception):
    pass

class Molekyl_syntax:
    def __init__(self, line_str):
        self.line_str = line_str
        self.index = 0

    def peek(self):
        if self.index < len(self.line_str):
            return self.line_str[self.index]
        return ""

    def pop(self):
        if self.index < len(self.line_str):
            i = self.line_str[self.index]
            self.index += 1
            return i
        return ""

    def readmol(self):
        self.read_whole_line()
        if self.peek() != "" and self.peek() != ")":#kollar om det är ) alltså fler )
            self.readmol()

    def read_line(self):
        self.readmol()
        if self.peek() != "":
            raise Syntaxerror("Felaktig gruppstart")
    
    def read_small_letter(self):
        self.pop()#problem om man återanvänder pga dequeue
    
    def readatom(self):
        atom_str = self.pop()  # Vi vet att detta är en stor bokstav pga read_whole_line
        
        if self.peek().islower():
            atom_str += self.pop()
            
        if atom_str not in atom_list:
            raise Syntaxerror("Okänd atom")
    
    def readnum(self):
        o = self.peek()

        if o == "0":
            self.pop()
            raise Syntaxerror("För litet tal")
        
        number_str = ""
        while self.peek().isdigit():
            number_str += self.pop()
        
        if not number_str:
            raise Syntaxerror("Saknad siffra")
        if int(number_str) < 2:
            raise Syntaxerror("För litet tal")
    
    def get_remaining(self):
        return self.line_str[self.index:]

    def read_whole_line(self):
        j = self.peek()#kollar 
        if j == "(":#kollar om ( sedan om det är )
            self.pop()
            self.readmol()
            if self.peek() == ")":#kollar om ) sedan kollar numret det är
                self.pop()
                self.readnum()#läsnummer
            else:
                raise Syntaxerror("Saknad högerparentes")
            
        elif j.isalpha() and j.isupper():#kollar om enbart bokstäver och om det är uppper 
            self.readatom()
            if self.peek().isdigit():
                self.readnum()

        elif j.isalpha() and j.islower():
            raise Syntaxerror("Saknad stor bokstav")
        
        else:
            raise Syntaxerror("Felaktig gruppstart")
def check_for(fstr):
    if fstr == "#":
        return ""
    m = Molekyl_syntax(fstr)
    try:
        m.read_line()
        return "Formeln är syntaktiskt korrekt"
    except Syntaxerror as e:
        return f"{e} vid radslutet {m.get_remaining()}"

def main():
    while True:
        try:#startar
            while True:
                line = input().strip()
                
                if line =="#":
                    break

                hypotes_molekyl = Molekyl_syntax(line)

                try:
                    hypotes_molekyl.read_line()
                    print("Formeln är syntaktiskt korrekt")
                except Syntaxerror as e:
                    print(f"{e} vid radslutet {hypotes_molekyl.get_remaining()}")
        except:
            break


#main()
class TestMole(unittest.TestCase):
    def test_del1(self):
        self.assertEqual(check_for("Na"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_for("H2O"), "Formeln är syntaktiskt korrekt")
    
    def test_del2(self):
        self.assertEqual(check_for("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
        self.assertEqual(check_for("Nacl"), "Saknad stor bokstav vid radslutet cl")


unittest.main()