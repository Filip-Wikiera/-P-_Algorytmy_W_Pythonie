# ---------------------------------------------------------------------------------
class Element:
    def __init__(self, pDane, pNastepny=None):
        self.dane = pDane
        self.nastepny = pNastepny

    def wypiszElementy(self):
        tmp = self
        while tmp != None:
            print(tmp.dane, end=" ")
            tmp = tmp.nastepny
    print("\n")
# ---------------------------------------------------------------------------------
class Lista:
    def __init__(self):
        self.glowa = None
        self.ogon = None

    def wstawNaKoniec(self, pDane):
        x = Element(pDane)
        if (self.glowa == None):
            self.glowa = x
            self.ogon = x
        else:
            self.ogon.nastepny = x
            self.ogon = x

    def wypisz(self):
        tmp=self.glowa
        if tmp == None:
            print("\n *Lista pusta*")
            return
        while tmp != None:
            print(tmp.dane, end=" ")
            tmp = tmp.nastepny
        print("\n")

    def szukaj(self, x):
        tmp = self.glowa
        while tmp != None:
            if tmp.dane == x:
                print("\nZnalazłem poszukiwany element ", x)
                return
            tmp = tmp.nastepny
        if tmp == None:
            print("\nNie znaleziono poszukiwanego elementu ", x)

    def dlugosc(self):
        licz = 0
        tmp = self.glowa
        while tmp != None:
            licz+=1
            tmp = tmp.nastepny
        return licz

    def zwroc_po_ID(self, id:int):
        tmp = self.glowa
        if tmp == None or id < 0 or id >= self.dlugosc():
            raise Exception("Blad wprowadzonych danych!")

        i = 0
        while tmp != None and i <=id:
            if i == id: return tmp

            i+=1
            tmp = tmp.nastepny

        return None

    def usun_po_ID(self, id:int):

        if id < 0 or id >= self.dlugosc(): raise Exception("Blad wprowadzonych danych!")
        elif self.glowa == None: return False
        elif id == 1:
            self.glowa = self.glowa.nastepny
            return True
        else:
            i = 0
            tmp = self.glowa
            tmp_poprzedni = self.glowa
            while tmp != None and i <= id:
                if i == id:
                    tmp_poprzedni.nastepny = tmp.nastepny
                    return True
                i += 1
                tmp_poprzedni = tmp
                tmp = tmp.nastepny


lista = Lista()
for i in range(10):
    lista.wstawNaKoniec(i)
lista.wypisz()
print(f"Liczba elementow w zbiorze: {lista.dlugosc()}")
print(f"Element na pozycji 3:{lista.zwroc_po_ID(3).dane}")
print(f"Element na pozycji 5:{lista.zwroc_po_ID(5).dane}")
print(f"Element na pozycji 7:{lista.zwroc_po_ID(7).dane}")

try:
    print(f"Element na pozycji 20:{lista.zwroc_po_ID(20).dane}")
except:
    print("Blad!")

print(lista.usun_po_ID(3))
lista.wypisz()
print(lista.usun_po_ID(3))
lista.wypisz()
