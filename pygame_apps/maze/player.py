from typing import Tuple

from pygame.surface import Surface

from pygame_apps.maze.actor import Actor

# enum TipObiect {
#     CHEIE,
#     BAT,
# }


from enum import Enum
class ObjectType(Enum):
    SEED = 1
    STICK = 2
    KEY = 3


class PickedObject:
    def __init__(self, mass: int, type: ObjectType, text: Surface, pos: Tuple[int, int]):
        self.mass = mass
        self.type = type
        self.text = text
        self.pos = pos

# if __name__ == '__main__':
#     secret_key = PickedObject(300, ObjectType.KEY)
#
#     if secret_key.type == ObjectType.SEED:
#         print('we found a key')


class Player:
    """
    Metode player-ului: (ce ii poti spune jucatorului sa faca)
        fly/move          towards a direction
        eat               se opreste pentru 3 secunde, daca nu dam nicio alta comanda, primeste energia la loc
        stand still  ->   primeste energie, 20% pentru fiecare secunda

        sa spunem ca va cara un anumit obiect si consuma mai multa energie in acel moment
        =>  date     pierzi energie mai multa,      in functie de greutatea obiectului, pierzi energie. 100, 200, 300 grame => 20%, 30%, 40% scade energie mai rapid
                                                            samanta, bat mic, cheie
        actiune=ridica obiecte
    Date:
        nivelul de energie ->       energie_curenta, energie maxima   2 float-uri
        pentru numarul de inimi ->  doua int-uri pentru numarul maxim si numarul curent

        pozitia: tuplu de doi intregi  (x,y)

        obiect ridicat  (tip, greutate)

    """
    def __init__(self, actor: Actor, ):
        pass