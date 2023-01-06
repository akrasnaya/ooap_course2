# КЛАСС ДВИГАТЕЛЬ
class Engine():
    #КОНСТРУКТОР
    def __init__(self, power, type):
        self.power = power # МОЩНОСТЬ
        self.type = type # ТИП ДВИГАТЕЛЯ

# КЛАСС МАШИНА
class Machine():
    # КОНСТРУКТОР
    def __init__(self, num, type, brand, power, eng_type):
        self.win_num = num # СЕРИЙНЫЙ НОМЕР
        self.type = type # ТИП МАШИНЫ (ЗДЕСЬ МОЖЕТ БЫТЬ КАК СТРОИТЕЛЬНЫЙ КРАН, ТАК И ПОСУДОМОЙКА)
        self.brand = brand # БРЕНД МАШИНЫ
        self.engine = Engine(power, eng_type) # ДВИГАТЕЛЬ МАШИНЫ (ПРИМЕР КОМПОЗИЦИИ)

# КЛАСС АВТОМОБИЛЬ
class Car(Machine): # ПРИМЕР НАСЛЕДОВАНИЯ, АВТОМОБИЛЬ - ТОЖЕ МАШИНА
    # КОНСТРУКТОР
    def __init__(self, num, type, brand, power, eng_type, color, complection):
        super(Car, self).__init__(num, type, brand, power, eng_type) # ЗДЕСЬ ПЕРЕОПРЕДЕЛЯЕТСЯ КОНСТРУКТОР
        # КЛАССА MACHINE, TYPE ЗДЕСЬ - ТИП КУЗОВА АВТОМОБИЛЯ
        self.color = color # ЦВЕТ АВТОМОБИЛЯ
        self.complection = complection # КОМПЛЕКТАЦИЯ ИЛИ ОПЦИИ АВТОМОБИЛЯ

