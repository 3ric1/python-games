# This is OOP!

# Pentru a ne fi mai usor sa lucram cu librarii, ne insusim baza Programării Orientate pe Obiecte
# .. este doar o modalitate diferită de a gândi și organiza codul ;)

# Discutie despre lista, ca obiect :D
# l = []
# l.append(2)  # cum functioneaza -> este o metoda, adica o functie legata (bind) de un obiect (l)
# print(l)
# l + [2,3]
# l.__add__([2,3])  # exemplu de metode magica

# int, float, dict, tuple, str    sunt tot obiecte      cream un int, float, dict, str prin a ascrie int('23') sau str(23)


# Nivelul 1
#
# Cum putem reprezenta un obiect?


# 1.1

# # Avem n produse. Fiecare produs are un pret, dar si o denumire.
# denumiri = ['Mouse', 'Unitate', 'Ochelari de soare', 'Raft']  # spunem ceva, si facem altceva (doua liste)
# preturi = [32, 220, 29.99, 32.90]
#
# # parcurgerea lor
# print("Produsele noastre:")
# print("------------------")
# for nume, pret in zip(denumiri, preturi):
#     print(f'{nume}: {pret}')


# Discrepanta?
# in viata reala ni se spune ca avem un numar de produse (logic, fiecare produs in parte are un pret si o denumire)
# dar in program trebuie sa facem o lista cu denumiri si o lista cu preturile fiecaruia


# Solutia OOP?
# TODO sa avem o **schema** pentru produs:
class Produs:
    # scrie "def init" si apasa Tab. TODO try it :)

    # 1. toate metodele magice, contin primul argument self
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret

    # def __init__(self, nume, pret):  # aici introducem datele obiectului
    #     # in metoda, copiem argumentele in self:
    #     self.nume = nume
    #     self.pret = pret

    def __str__(self):  # aici spunem cum afisam obiectul, cand apelam  str(p)
        return f'nume={self.nume},pret={self.pret}'

    def __repr__(self):  # aici spunem cum afisam obiectul, intr-o lista
        return f'Produs(nume={self.nume},pret={self.pret})'


# p = Produs("Servetele", 6.99)
# print(p.pret, p.nume)  # pret si nume sunt denumite campuri (fields)
# p.pret = 3
# print(p.pret, p.nume)  # pret si nume sunt denumite campuri (fields)
# # p.pret = '----'  # POSIBIl, nu recomandat
# # print(p.pret, p.nume)  # pret si nume sunt denumite campuri (fields)

# TODO va fi mai logic sa cream o lista de Produse
# sa citim n produse. Fiecare produs cu nume si pret, si sa le retinem intr-o lista.

'''
3
Servetele
6.99
Batiste
9.99
Hartie pentru copiere
13.99
'''


def main():
    n = int(input())
    lista = []
    for i in range(n):
        # citim un produs (nume + pret)
        nume = input()
        pret = float(input())
        p = Produs(nume, pret)
        # il putem adauga in lista
        lista.append(p)
    print(lista)
    print(lista[0])
    # print(reversed([1, 2, 3]))


# if __name__ == '__main__':
#     main()

# 1.1.2

# folosim ce am lucrat ca exercitiul 1.1 pentru a crea o functie care citeste o lista de produse.
# Se cere:
#  a) afisarea celui mai scump produs
#  b) afisare  produselor  in ordine lexicografica a numelui(fie folosind 2 for-uri, fie folosind sort())

def citeste_n_produse():
    n = int(input())
    lista = []
    for i in range(n):
        # citim un produs (nume + pret)
        nume = input()
        pret = float(input())
        p = Produs(nume, pret)
        # il putem adauga in lista
        lista.append(p)
    return lista


'''
3
Servetele
6.99
Batiste
9.99
Hartie pentru copiere
13.99
'''


# # TODO Reamintinre lambda functions (or anonymous functions)
# def f1(x):
#     return x * 2
#
#
# f2 = lambda x: x * 2  # inainte de : sunt argumentele unei functii, iar dupa : este valoarea returnata
#
# print(f1(3), f2(3))

def main():
    l = citeste_n_produse()

    # argumentul key=  este "valoarea" folosita la compararea elementelor din lista
    # deci noi ii spunem, pt fiecare x din lista, nu-l compara cu alte produse, ci compara doar x.preet (adica pretul produselor)
    print('a)', max(l, key=lambda x: x.pret))  # am definit o functie care primeste un x, si returneaza x.pret

    #  b) afisare  produselor  in ordine lexicografica a numelui(fie folosind 2 for-uri, fie folosind sort())
    a = 'mihai, maria, alex'.split(', ')
    a.sort()
    print(a)
    l.sort(key=lambda x: x.nume)
    print('b)', l)


# if __name__ == '__main__':
#     main()


# 1.2

class Stilou:
    '''
    Stiloul va avea o firma, o denumire proprie si pretul
    '''

    # scrie "def init" si apasa Tab. TODO try it :)

    # TODO     def init
    #          def str
    #          def repr

    def __init__(self, nume, pret, firma):  # denumit si constructor
        self.nume = nume
        self.pret = pret
        self.firma = firma

    def __str__(self):
        # returnam un string care contine datele produsului
        # e.g.    "Stiloul de firma=Schneider cu pret=23, nume='Roller'"
        date = f"firma = {self.firma}, nume = {self.nume}, pret = {self.pret}"
        return date


# stilou = Stilou('dw11', 5.80, 'Dedeman')  # in Stilou() folosesti init din clasa
# print(stilou)  # cand dai print, converteste la str, deci foloseste str() din clasa


# TODO sa cream o functie care citeste de la tastatura datele unui Stilou,
#  dupa care returneaza noul stilou

def citire_stilou():
    nume = input('> nume: ')
    pret = float(input('> pret: '))
    firma = input('> firma: ')
    p = Stilou(nume, pret, firma)
    return p


def main():
    l = citire_stilou()
    print(l)


# if __name__ == '__main__':
#     main()

# 1.3
# TODO sa cream o clasa denumite Fractie pe care o vom folosi pentru a retine o fractie
#  -> numarator si numitor
# TODO
#  Sa cream un program care citeste o lista de n numere intregi,
#   dupa care va afisa toate fractiile obtinute cu orice doua numere din lista

# e.g
# 3
# 1 2 3
# fractiile: 1/1 1/2  1/3  2/1 2/3 3/2    scopul este sa si elimina fractiile duplicate (e.g. 1/1 == 2/2 deci nu afisam si 2/2)

class Fractie:
    def __init__(self, numitor, numarator):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):  # apelat cand scrii print(f) sau str(f)
        fractii = f'{self.numarator}/{self.numitor}'  # 23/4
        return fractii

    def __repr__(
            self):  # este folosit cand afisam o lista care contine Fractii. Ar fi o denumire mai scurta, ca sa fie usor de citit lista afisata
        # return self.__str__()
        fractii = f'{self.numarator}/{self.numitor}'  # 23/4
        return fractii

    # daca nu avem eq, cand egaleaza doua fractii ca sa afle daca sunt egale, foloseste adresa din memorie a variabilelor.
    def __eq__(self, other):
        a1 = self.numarator
        b1 = self.numitor
        a2 = other.numarator
        b2 = other.numitor
        # returnam True daca a1/b1 este egal cu a2/b2
        # altfel False
        return a1 * b2 == a2 * b1


# print(Fractie(2,3))

def main():
    lista = []
    numere = []
    n = int(input())
    for i in range(n):
        x = int(input())
        numere.append(x)
    for i in range(n):
        for j in range(n):
            numarator = numere[i]
            numitor = numere[j]
            p = Fractie(numarator, numitor)
            lista.append(p)
    print(lista)

    # # filter? sau list comprehension cu if
    # l = [
    #      f for f in lista
    #      if lista.count(f) == 1  # pastram doar elementele care apar o singura data
    # ]

    # facem o lista goala, si adaugam doar elementele pe care inca nu le-am adaugat

    l = []
    for f in lista:
        # daca in l nu exista f-ul, il adaugam
        if l.count(f) == 0:  # foloseste __eq__ ca sa compare doua Fractii
            l.append(f)
    print(l)


# if __name__ == '__main__':
#     main()


# 1.4  Avem si noutate: libraria random
#
# In jocuri, dar si in alte aplicatii uzuale, avem nevoie de valori random
#  ( pentru a decide cine este primul jucator, pentru a putea avea un AI chiar si in jocuri simple
#    precum X si 0 etc )

# vom folosi random.randint pentru a crea o lista cu n intregi, valori intre 0 si 3
#
# Consideram:
#  0 -> N
#  1 -> E
#  2 -> S
#  3 -> V
# Sa le folosim pentru a afisa pozitia finala a unui omulet,
#  daca la inceput se afla in coordonatele 0, 0
# E.g. daca se va genera 0 0 1 3
#  omuletul parcurge pe rand pozitiile (0,0) -> (0, 1) -> (0,2) -> (1,2) iar in final (0,2)
#
#  Deci se va afisa mesajul:
#  0 2


'''
Se citesc de la tastatură 6 variabile, denumite an1, luna1, ziua1, an2, luna2, ziua2, care vor reprezenta două date calendaristice.

Se cere să afișați:

a) Care dintre cele două date calendaristice este mai mare?
b) Care dintre cele două date calendaristice este mai apropiată de ziua de astăzi?

E.g.

2 10 2021
3 9 2021
a) Data 2.10.2021 este mai mare
b) Data 2.10.2021 este mai apropiată

7 2 2022
25 2 2022
a) Data 25.2.2022 este mai mare
b) Data 7.2.2022 este mai apropiată

'''


class Data_Calendaristica():
    def __init__(self, ziua, luna, an):
        self.ziua = ziua
        self.luna = luna
        self.an = an

    def __str__(self):
        data = f'{self.ziua}.{self.luna}.{self.an}'
        return data

    def __repr__(self):
        return str(self)

    # var. 2
    '''
    Exemplu la liste:
    l = [1,2,3]
    l.append(5)
    
    '''

    def este_mai_mare(self: 'Data_Calendaristica', d2: 'Data_Calendaristica'):  # functii interne sunt numite metode
        d1 = self
        if d1.an > d2.an:
            return True
        elif d1.an == d2.an:
            if d1.luna > d2.luna:
                return True
            elif d1.luna == d2.luna:
                if d1.ziua > d2.ziua:
                    return True
        return False

    '''
    metoda care calculeaza cate zile vor trece pana ajunge din data curenta, la o alta data
    
    d1 = 23.10.2003
    d1 = 23.10.2004   # +366 zile     # an bisect = se divide cu 4, dar nu se divide cu 400
    d1 = 23.10.2005   # 366+365=631 zile
    d1 = 23.10.2006   # 366+365=631 zile
    ...
    d1 = 23.10.2022   # crestem luna, dar haide prima data sa aduce la inceputul lunei urmatoare
    d1 = 1.11.2022   # crestem luna, dar haide prima data sa aduce la inceputul lunei urmatoare
    # ori cresti cu diferenta in zile, ori scazi diferenta in zile
    
    d2 = 24.11.2022
    '''

    def diferenta_in_zile(self: 'Data_Calendaristica', d2: 'Data_Calendaristica'):
        from copy import copy
        d1 = copy(self)

        aux = 0
        while d1.an != d2.an:
            if d1.an > d2.an:
                d1.an -= 1
                aux -= 365
                if d1.an % 4 == 0 and d1.an % 400 != 0:
                    aux -= 1
            else:
                d1.an += 1
                aux += 365
                if d1.an % 4 == 0 and d1.an % 400 != 0:
                    aux += 1

        if d1.an % 4 == 0 and d1.an % 400 != 0:
            numar_luni = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            numar_luni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # daca d1 < d2  sa crestam d1 pana la prima zi din luna urmatoare
        # altfel il scadem pe d1 pana la prima zi din luna curenta
        if d1.luna < d2.luna:
            aux += numar_luni[d1.luna - 1] - d1.ziua + 1
            d1.luna += 1
            d1.ziua = 1
        elif d1.luna > d2.luna:
            aux -= numar_luni[d1.luna - 2] + d1.ziua - 1
            d1.luna -= 1
            d1.ziua = 1

        if d1.luna < d2.luna:
            while d1.luna != d2.luna:
                aux += numar_luni[d1.luna - 1]
                d1.luna += 1
        else:
            while d1.luna != d2.luna:
                aux -= numar_luni[
                    d1.luna - 1 - 1]  # de pe 1 feb => 1 ianuarie sunt numarul de zile ale lui ianuarie, nu februarie
                d1.luna -= 1

        if d1.ziua < d2.ziua:
            aux += d2.ziua - d1.ziua
            d1.ziua += d2.ziua - d1.ziua

        elif d1.ziua > d2.ziua:
            aux -= d1.ziua - d2.ziua
            d1.ziua -= d1.ziua - d2.ziua

        return aux


# var. 1  - deja cunoscuta - cream o functie globala (in afara clasei
def este_mai_mare(d1: Data_Calendaristica, d2: Data_Calendaristica):
    if d1.an > d2.an:
        return True
    elif d1.an == d2.an:
        if d1.luna > d2.luna:
            return True
        elif d1.luna == d2.luna:
            if d1.ziua > d2.ziua:
                return True
    return False


# d1, d2, data_curenta

# l = [1,2,3]
# l.__contains__(2)  # folosit de fapt ca    2 in l
# l.__len__()  # dar noi folosim   len(l) ca sa fie mai usor de citit
#
# # # init este folosit pt create de obiecte
# # d = Data_Calendaristica(20, 4, 2003) # __init__
# # print(d)  # __str__

def main():
    # ziua1 = int(input())
    # luna1 = int(input())
    # an1 = int(input())
    # ziua2 = int(input())
    # luna2 = int(input())
    # an2 = int(input())
    #
    # # cream doua date
    # d1 = Data_Calendaristica(ziua1,luna1,an1)
    # d2 = Data_Calendaristica(ziua2,luna2,an2)
    #
    #
    # # si vom crea in clase metode (functii) utile
    # print(este_mai_mare(d1,d2)) # d1 > d2
    # print(d1.este_mai_mare(d2)) # d1 > d2

    d1 = Data_Calendaristica(22, 2, 2022)
    d2 = Data_Calendaristica(20, 2, 2022)
    azi = Data_Calendaristica(23, 2, 2022)
    # print(d1.diferenta_in_zile(d2))

    if d1.diferenta_in_zile(azi) > d2.diferenta_in_zile(azi):
        print(d2)
    else:
        print(d1)


# # Todo de facut afisarea pentru subpunctul b)
# # Todo b) Care dintre cele două date calendaristice este mai apropiată de ziua de astăzi?
# if __name__ == '__main__':
#     main()


# class Fractii():
#     def __init__(self,numitor,nu):
#
#
# def main():
#     n = int(input())
#     nr = []
#     for i in range(n):
#         x = int(input())
#         nr.append(x)

class Bilet:
    def __init__(self, nume_calator='', are_clasa1=False):  # =False si =''  sunt valori default (implicite)
        self.nume_calator = nume_calator
        self.are_clasa1 = are_clasa1

    def __str__(self):
        bilete = f'{self.nume_calator},{self.are_clasa1}'
        return bilete

    def __repr__(self):
        return str(self)

    def citeste(self):
        self.nume_calator = input()
        self.are_clasa1 = True if input() == "True" else False


# if __name__ == '__main__':
#     n = int(input())
#
#     bilete = [Bilet() for _ in range(n)]
#     for bilet in bilete:
#         bilet.citeste()
#
#     print(bilete)

def statisticaZboruri(bilete):
    contor1 = 0
    contor2 = 0
    for bilet in bilete:
        if bilet.are_clasa1 == True:
            contor1 += 1
        else:
            contor2 += 1
    print(f'Avem {contor1} bilete la clasa I, dar si {contor2} la alte clase.')


def main():
    bilete = [Bilet("Popescu Leuraș", True),
              Bilet("Manolescu Alexandra", True),
              Bilet("Popescu Mănăila", False)]
    statisticaZboruri(bilete)

# if __name__ == '__main__':
#     main()



class Tablou:
    def __init__(self,inaltime=0,pret=0,mesaj_motivational=''):
        self.inaltime = inaltime
        self.pret = pret
        self.mesaj_motivational = mesaj_motivational

    def __str__(self):
        tablouri = f'{self.inaltime},{self.pret},{self.mesaj_motivational}'
        return tablouri

    def __repr__(self):
        return str(self)

    def citeste(self):
        self.inaltime = int(input('Inaltime:'))
        self.pret = int(input('Pret:'))
        self.mesaj_motivational = input("Mesaj motivational: ")

def aflare_numar_cuvinte(mesaj):
    # numaram cate cuvinte are string-ul mesaj
    # putem folosi re pentru a gasi/extrage toate cuvintele
    import re
    cuvinte = re.findall(r'\w+', mesaj)
    return len(cuvinte)
'''

'''

def main():
    n = int(input())
    # citim cele n tablouri
    tablouri = [Tablou()   for i in range(n)]
    for tablou in tablouri:
        tablou.citeste()
    print(tablouri)

    # sortam tablourile
    tablouri.sort(key=lambda x: aflare_numar_cuvinte(x.mesaj_motivational))

    # il afisam pe ultimul
    print(tablouri[-1])
    # for tablou in tablouri:
    #     v.append(aflare_numar_cuvinte(tablou.mesaj_motivational))
    # v.sort()
    # print(v[-1])

# if __name__ == '__main__':
#     main()

class Client:

    def __init__(self, ID_client='', suma=0):
        self.ID_client = ID_client
        self.suma = suma

    def __str__(self):
        clienti = f'{self.ID_client},{self.suma}'
        return clienti

    def __repr__(self):
        return str(self)

    def citire(self):
        self.ID_client = input('ID:')
        self.suma = int(input("Suma:"))



class Banca:

    def __init__(self, nr_clienti=0, clienti=[]):
        self.nr_clienti = nr_clienti
        self.clienti = clienti

    def __str__(self):
        banci = f'{self.nr_clienti},{self.clienti}'
        return banci

    def __repr__(self):
        return str(self)

    def citire(self):
        sum_tot = 0
        self.nr_clienti = int(input("Nr Clienti:"))
        self.clienti = [Client() for _ in range(self.nr_clienti)]
        for client in self.clienti:
            client.citire()

    def cantitate_totala(self):
        cantitate = 0
        for client in self.clienti:
            cantitate += client.suma
        return cantitate

    def minimum_1000(self):
        contor = 0
        for client in self.clienti:
            if client.suma >= 1000:
                contor += 1
        return contor

    def procente(self):
        nr = 0
        contor = 0
        for client in self.clienti:
            nr += 1
            if client.suma > 100:
                contor += 1
        return contor * 100 / nr


class Date:

    def __init__(self, an, luna, zi):
        pass

    # gt = supraincarcare de operator, inseamna     greater than
    # e folosit pt a spune codului cum sa ruleze    data1 > data2    adica ce valoarea sa calculeze rulam astfel de cod
    def __gt__(self, other):  # pentru cand scriem   data1  >  data2
        if self.an > other.an:
            return True
        if self.an < other.an:
            return False
        # similar pt luna si zi
        # TODO

class Event:
    def __init__(self, inceput, final):
        if inceput > final:
            final, inceput = inceput, final  # ca sa ne asiguram ca datile vor fi corecte
        self.inceput = inceput
        self.final = final

    def are_loc_dupa(self, event1):
        # evenimentul self se intampla dupa evenimentul 1, daca
        if self.inceput > event1.final:
            return True
        else:
            return False


# # vei sorta evenimentele dupa data de final
# l.sort(key=lambda x: x.final)  # necesita sa implementezi <  (__lt__) in Data
#         https://www.pythonpool.com/python-__lt__/

# def main():
#     # clienti = [
#     #     Client(),
#     #     Client()
#     # ]
#     # banca = Banca(len(clienti), clienti)
#     banca = Banca()
#     banca.citire()
#
#     print(banca.procente())
#     print(banca.cantitate_totala())
#     print(banca.minimum_1000())

if __name__ == '__main__':
    main()