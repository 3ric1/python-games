# cream o clasa care foloseste evenimentele din Pygame pentru a crea o clasa care ne raspunde
#  la intrebarea "care taste sunt apasate in mod prezent" si in acelasi timp, nu-si schimba directia daca este apasat si
#  left_arrow_key si right_arrow_key

# sau sa stea pe loc daca sunt amandoua apsate
from pygame.constants import KEYDOWN, KEYUP, K_UP
from pygame.event import Event


class PressedKeys:
    def __init__(self):
        self.pressed_keys = set()

    def update(self, events: list[Event]):
        for ev in events:
            if ev.type == KEYDOWN:
                print(ev.key)
                self.pressed_keys.add(ev.key)
            elif ev.type == KEYUP:
                if ev.key in self.pressed_keys:
                    self.pressed_keys.remove(ev.key)

    def __contains__(self, item):
        return item in self.pressed_keys

    def __str__(self):

        return f'Pressed( {self.pressed_keys} )'
