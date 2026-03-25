import sys

VALID_ATOMS = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv".split()

class Syntaxfel(Exception):
    pass

class MoleculeParser:
    def __init__(self, s):
        self.s = s
        self.idx = 0

    def peek(self):
        if self.idx < len(self.s):
            return self.s[self.idx]
        return ""

    def pop(self):
        if self.idx < len(self.s):
            c = self.s[self.idx]
            self.idx += 1
            return c
        return ""

    def get_remaining(self):
        return self.s[self.idx:]

    def readformel(self):
        self.readmol()
        if self.peek() != "":
            raise Syntaxfel("Felaktig gruppstart")

    def readmol(self):
        """<mol> ::= <group> | <group><mol>"""
        self.readgroup()
        # Rekursivt anrop till sig själv om vi inte nått strängslutet eller en parentes
        if self.peek() != "" and self.peek() != ")":
            self.readmol()

    def readgroup(self):
        c = self.peek()
        
        if c == "(":
            self.pop()
            self.readmol()
            if self.peek() == ")":
                self.pop()
                self.readnum()
            else:
                raise Syntaxfel("Saknad högerparentes")
                
        elif c.isalpha() and c.isupper():
            self.readatom()
            if self.peek().isdigit():
                self.readnum()
                
        elif c.isalpha() and c.islower():
            raise Syntaxfel("Saknad stor bokstav")
            
        else:
            raise Syntaxfel("Felaktig gruppstart")

    def readatom(self):
        atom = self.pop()
        
        if self.peek().isalpha() and self.peek().islower():
            atom += self.pop()
            
        if atom not in VALID_ATOMS:
            raise Syntaxfel("Okänd atom")

    def readnum(self):
        c = self.peek()
        
        if c == '0':
            self.pop()
            raise Syntaxfel("För litet tal")

        num_str = ""
        while self.peek().isdigit():
            num_str += self.pop()

        if not num_str:
            raise Syntaxfel("Saknad siffra")

        if int(num_str) < 2:
            raise Syntaxfel("För litet tal")

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
            
        parser = MoleculeParser(line)
        try:
            parser.readformel()
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            # Exception fångas och resterande kö skrivs ut
            print(f"{e} vid radslutet {parser.get_remaining()}")

if __name__ == '__main__':
    main()