#

class HashNode:
#Noder till klassen Hashtable

   def __init__(self, key = "", data = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:

   def __init__(self, size):
      """size: hashtabellens storlek"""
      self.size = size
      self.slots = [None] * self.size
      #print("New size:", size)

   def store(self, key, data):
      """key är nyckeln
         data är objektet som ska lagras
         Stoppar in "data" med nyckeln "key" i tabellen."""
      #Fyll i kod här!
      hashvalue = self.hashfunction(key)

      if self.slots[hashvalue] == None:
         self.slots[hashvalue] = HashNode(key, data)
      else:
         if self.slots[hashvalue].key == key:#kollar om key är samma
            self.slots[hashvalue].data = data#uppdatering av det som stod som data i key
         else:
            next_av_slot = self.rehash(hashvalue)
            while self.slots[next_av_slot] is not None and self.slots[next_av_slot].key != key:#försökeer hitta en plats
               next_av_slot = self.rehash(next_av_slot)
               if next_av_slot == hashvalue:
                  raise Exception("Full")
            
            if self.slots[next_av_slot] is None:#hittat en ledig plats lägg in den
               self.slots[next_av_slot] = HashNode(key, data)
            else:#hittade nyckeln
               self.slots[next_av_slot].data = data
      #print(f"{key} <- {data}")


   def search(self, key):
      """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
      #Fyll i kod här!
      #...
      start_slot = self.hashfunction(key)
      state = False#kollar om vi hittat nyckeln
      data = None
      stop = False#kollar om man ska sluta
      position = start_slot

      while self.slots[position] is not None and not state and not stop:
         if self.slots[position].key == key:#hittat nyckeln
            state = True
            data = self.slots[position].data
         else: 
            position = self.rehash(position)#nästa psition
            if position == start_slot:#om man gått ett helt varv ge upp
               stop = True


      if state:
         #print(f"{key}: {data}")
         return data
      else:
         #print(f"Keyerror: {key}")
         raise KeyError(key)



   def hashfunction(self, key):
      """key är nyckeln
         Beräknar hashfunktionen för key"""
      #Fyll i kod här!
      sum = 0
      for char in key:
         sum = sum*31 + ord(char)
      return sum % self.size
   
   def rehash(self, oldhash):
      return (oldhash + 1) % self.size
