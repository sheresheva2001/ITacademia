# Создайте  модель из жизни. Это может быть бронирование комнаты в
# отеле, покупка билета в транспортной компании, или простая РПГ.
# Создайте несколько объектов классов, которые описывают ситуацию.
# Объекты должны содержать как атрибуты так и методы класса для
# симуляции различных действий. Программа должна инстанцировать
# объекты и эмулировать какую-либо ситуацию - вызывать методы,
# взаимодействие объектов и т.д.

# создание РПГ


class Warrior:
    def __init__(self, health, stamina):
        self.health = health
        self.stamina = stamina

    def introduces(self):
        print('-------------------')
        print(f'class:{self.__class__.__name__}')
        print(f'healht:{self.health}')
        print(f'stamina:{self.stamina}')
        print('-------------------')

    def heals(self, target):
        print('-------------------')
        print(f'{self.__class__.__name__} накладывает повязку '
              f'{target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровье у {target.__class__.__name__} увеличилось на '
              f'{target.health}')
        print(f'{self.__class__.__name__} осталось {self.stamina} едениц силы')
        print('-------------------')

    def attacks(self, Mage):
        print('-------------------')
        print(f'{self.__class__.__name__} аттакует {Mage.__class__.__name__}'
              f'в результате противник теряет здоровье на 3 еденицы :{Mage.heals}')
        Mage.healt -= 3
        print('-------------------')



class Mage:
    def __init__(self, healt, mana):
        self.healt = healt
        self.mana = mana

    def introduces(self):
        print('-------------------')
        print(f'class:{self.__class__.__name__}')
        print(f'healht:{self.healt}')
        print(f'mana:{self.mana}')
        print('-------------------')

    def heals(self, target):
        print('-------------------')
        print(f'{self.__class__.__name__} принимает заклинание лечения к '
              f'{target.__class__.__name__}')
        target.healt += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} увеличилось на '
              f'{target.health}')
        print(f'У {self.__class__.__name__} осталось '
              f'{self.mana} единиц магии')
        print('-------------------')

    def attacks(self, Warrior):
        print('-------------------')
        print(f'{self.__class__.__name__} аттакует {Warrior.__class__.__name__}'
              f'в результате противник теряет здоровье на 3 еденицы :{Warrior.health}')
        Warrior.health -= 3
        print('-------------------')



unit1 = Warrior(health=90, stamina=100)
unit1.introduces()

unit2 = Mage(healt=00, mana=100)
unit2.introduces()

unit2.attacks(unit1)
unit1.attacks(unit2)