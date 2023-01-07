# РОДИТЕЛЬСКИЙ КЛАСС - МОТОЦИКЛ
class Bike():
    def __init__(self, num, brand, power):
        self.num = num #СЕРИЙНЫЙ НОМЕР
        self.brand = brand # МАРКА
        self.power = power # МОЩНОСТЬ

    def ride(self):
        print('just ride a bike')

# КЛАСС-НАСЛЕДНИК - ГОНОЧНЫЙ МОТОЦИКЛ (ЧАСТНЫЙ СЛУЧАЙ)
class SportBike(Bike):
    def __init__(self, num, brand, power, type):
        super(SportBike, self).__init__(num, brand, power)
        self.type = type # ТИП ГОНОК, В КОТОРЫХ МОЖЕТ ИСПОЛЬЗОВАТЬСЯ МОТОЦИКЛ

    def ride(self):
        print(f'riding the bike only on {self.type} races')

# КЛАСС-НАСЛЕДНИК ТРАНСПОРТНОЕ СРЕДСТВО (ОБЩИЙ СЛУЧАЙ)
class Transport(Bike):
    def __init__(self, num, brand, power, type, id, owner, color):
        super(Transport, self).__init__(num, brand, power)
        self.type = type # ТИП ТРАНСПОРТНОГО СРЕДСТВА
        self.id = id # РЕГИСТРАЦИОННЫЙ НОМЕР
        self.owner = owner # ИНФОРМАЦИЯ О ВЛАДЕЛЬЦЕ
        self.color = color

    def ride(self):
        print(f'riding the {self.color} {self.brand} with num {self.id}')

# КЛАСС-НАСЛЕДНИК МАСТЕРСКАЯ ДЛЯ СПОРТИВНЫХ МОТОЦИКЛОВ
class SportBikeRepairShop(Transport, SportBike):
    def __init__(self, num, brand, power, type, id, owner, color):
        super(SportBikeRepairShop, self).__init__(num, brand, power, type, id, owner, color)
    
    def repair(self):
        print(f'repairing bike {self.brand} {self.type} from {self.owner}')
    
    def ride(self):
        super(SportBike, self).ride(self)
