# Exercitii fara OOP

# 1. Cititi e la tastatura doua siruri de numere intregi, de aceiasi lungime.
#    Afisati suma maxima a n fractii care se pot forma folosind toate cele 2*n numere
#    Afisati si fractiile.

#  1, 2 , 3 , 4
#  9, 8 , 7 , 6
# 1/9 + 2/8 + 3/7 + 4/6 - merge pentru minim
# 9/1 + 8/2 + 7/ 3+ 6/4
'''
4
1 2 3 4
5 6 7 8
'''
from typing import List


def main():
    n = int(input())
    v = []
    s = 0
    rand = input().split()  # primul rand   =>     ['1', '2', '3', '4']
    for x in rand:
        v.append(int(x))
    rand2 = input().split()
    for x in rand2:
        v.append(int(x))
    v.sort(reverse=True)
    for i in reversed(range(n)):
        f = v[i] / v[-i-1]
        s += f
        print(f'{v[i]} / {v[-i-1]}')
    print(s)
# if __name__ == '__main__':
#     main()

# 2. Gasiti linia de pe o matrice care contine elementele de suma maxima.

"""
3
1 2 3
10 -9 1
3 4 0

"""

def suma_max(m):
    n = len(m)  #    n2 = len(m[0])
    maxim = 0
    for i in range(n):
        # sum(m[0]) # suma elementelor de pe prima linie
        suma = sum(m[i])
        if maxim < suma:
            maxim = suma
            aux = i + 1
    return aux

def main():
    m = []
    n = int(input())
    for i in range(n):
        # creeze linia noua:
        linie_noua = []
        # adaugam in lista elementele de pe un rand
        rand = input().split()  # '1 2 3'
        for x in rand:
            linie_noua.append(int(x))
        # adaugam in matrice linia
        m.append(linie_noua)
    print(suma_max(m))
# if __name__ == '__main__':
#     main()


# Exercitii cu OOP

# Avantaje?
# * Pastram datele ascunse. si unite
# * Putem implementa operatii pe un anumit tip de date mai complex (e.g. utilizatori)

class Elev:
    def __init__(self, note: List[int], nume: str) -> None:  # in C++      void __init__(int[] note, char nume[] )
        self.note = note
        self.nume = nume

    # avantajul 2: putem crea metode (i.e. functii cu acces la datele din clasa)
    #              utile
    def medie(self):
        return sum(self.note) / len(self.note)

# if __name__ == '__main__':
#     elev = Elev([10, 9], "Eric")
#     print(elev.note, elev.nume)
#     print(elev.medie())

# Exemplu:
"""
Creați o clasa UserLogin care va reține următoarele date despre un utilizator, pe
 care a completat un formular de logare:

* lastname      - numele
* firstname     - prenumele
* password      - parola introdusa
* rpassword     - confirmarea parolei introduse
* age        - un numar

Dupa ce ati creat clasa (constructor, proprietati, metoda str()), adaugati urmatoarea
 metoda:

 def verify_password_confirm():
    pass # returneaza True daca confirmarea parolei este corecta
"""

class UserLogin:
    def __init__(self, lastname: str, firstname: str, password: str, rpassword: str, age: int):
        self.lastname = lastname
        self.firstname = firstname
        self.password = password
        self.rpassword = rpassword
        self.age = age
    def verify_password_confirm(self):
        if self.password == self.rpassword:
            return True
        return False


if __name__ == '__main__':
    user_data = UserLogin("Paturan", "Eric", "parola", "parol1", 15)
    print(user_data.verify_password_confirm())

