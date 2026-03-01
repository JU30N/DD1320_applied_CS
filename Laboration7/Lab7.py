
from hashtable import Hashtable

class DictHash:
    def __init__(self):
        self._dict = {}

    def store(self, key, data):
        self._dict[key] = data

    def search(self, key):
        if key in self._dict:
            return self._dict[key]
        

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        return key in self._dict
    
class Drama:
    def __init__(self, DramaName, Rating, Actors, ViewshipRate, Genre):
        self.DramaName = DramaName
        self.Rating = Rating
        self.Actors = Actors
        self.ViewshipRate = ViewshipRate
        self.Genre = Genre

    def __str__(self):
        return f"{self.DramaName}, {self.Rating}, {self.Actors}, {self.ViewshipRate}, {self.Genre}"

def main_del2():
    drama_table = Hashtable(20)
    with open(r"C:\Users\joong\Desktop\DD1320\DD1320_applied_CS\Laboration7\kdramaMini.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            #print(line)
            line_data = line.strip().split(",")
            #print(line_data)
            name = line_data[0]
            rating = line_data[1]
            actors = line_data[2]
            vsR = line_data[3]
            genre = line_data[4]
            drama_object = Drama(name, rating, actors, vsR, genre)
            drama_table.store(name, drama_object)#store name of the drama with the correspoding drama obj with all needed info
    sok = "The Heirs"
    try:
        result = drama_table.search(sok)
        print(f"söker: {sok}    Resultat: {result}")
    except:
        print("hittades ej")

def main_del1():
    drama_dict = DictHash()
    with open(r"C:\Users\joong\Desktop\DD1320\DD1320_applied_CS\Laboration7\kdramaMini.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            #print(line)
            line_data = line.strip().split(",")
            #print(line_data)
            name = line_data[0]
            rating = line_data[1]
            actors = line_data[2]
            vsR = line_data[3]
            genre = line_data[4]
            drama_object = Drama(name, rating, actors, vsR, genre)
            drama_dict.store(name, drama_object)#store name of the drama with the correspoding drama obj with all needed info 

    sok = "Goblin"
    try:
        result = drama_dict.search(sok)
        print(f"söker: {sok}    Resultat: {result}")
    except:
        print("hittades ej")



def main():
    hashtable = None
    
    while True:
        line = input()
        key, *value = line.split()
        if key == '#':
            print('#')
            break
        elif key == 'init' and len(value) > 0:
            size = int(value[0])
            hashtable = Hashtable(size)
            print('New size:', size)
        elif len(value) > 0:
            hashtable.store(key, value[0])
            print(key, '<-', value[0])
        else:
            try:
                value = hashtable.search(key)
                print(f'{key}: {value}')
            except KeyError:
                print('KeyError:', key)


if __name__ == "__main__":
    main()
