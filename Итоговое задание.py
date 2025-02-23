from abc import ABC, abstractmethod
# Первая сущность: транспорнтные средства
class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"Vehicle('{self.brand}', '{self.model}', {self.year})"

    def start_engine(self) -> str:
        return "Двигатель включен"

class Car(Vehicle):
    """
    Дочерний класс для авто.
    """

    def __init__(self, brand: str, model: str, year: int, passengers: int) -> None:
        super().__init__(brand, model, year)
        self.passengers = passengers

    def __str__(self) -> str:
        return f"Легковой автомобиль: {self.brand} {self.model} ({self.year}), {self.passengers} мест"

    def open_trunk(self) -> str:
        return "Багажник открыт"

class Truck(Vehicle):
    """
    Дочерний класс для грузовиков.
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: float) -> None:
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        return f"Грузовик: {self.brand} {self.model} ({self.year}), грузоподъемность {self.load_capacity} т"

    def start_engine(self) -> str:
        """
        Переопределение метода для грузовика, так как запуск двигателя может отличаться.
        """
        return "Грузовой двигатель включен с дополнительным прогревом"

# Вторая сущность: Животные
class Animal(ABC):
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Animal('{self.name}', {self.age})"

    @abstractmethod
    def make_sound(self) -> str:
        pass

class Dog(Animal):
    """
    Дочерний класс для собак.
    """

    def make_sound(self) -> str:
        return "Гав-гав!"

class Cat(Animal):
    """
    Дочерний класс для кошек.
    """

    def make_sound(self) -> str:
        return "Мяу!"

# Третья сущность: Гаджеты
class Gadget:
    """
    Базовый класс для гаджетов.
    """

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f"Гаджет: {self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"Gadget('{self.brand}', '{self.model}')"

    def turn_on(self) -> str:
        return "Гаджет включен"

class Smartphone(Gadget):
    """
    Дочерний класс для смартфонов.
    """

    def __init__(self, brand: str, model: str, os: str) -> None:
        super().__init__(brand, model)
        self.os = os

    def __str__(self) -> str:
        return f"Смартфон: {self.brand} {self.model} на {self.os}"

    def take_photo(self) -> str:
        return "Фотография сделана"

class Laptop(Gadget):
    """
    Дочерний класс для ноутбуков.
    """

    def __init__(self, brand: str, model: str, ram: int) -> None:
        super().__init__(brand, model)
        self.ram = ram

    def __str__(self) -> str:
        return f"Ноутбук: {self.brand} {self.model} с {self.ram} ГБ ОЗУ"

    def turn_on(self) -> str:
        """
        Переопределение метода включения, так как ноутбук проходит процесс загрузки.
        """
        return "Ноутбук загружается..."


if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2022, 5)
    truck = Truck("Volvo", "FH16", 2020, 20.5)
    dog = Dog("Шарик", 3)
    cat = Cat("Мурка", 2)
    phone = Smartphone("Apple", "iPhone 13", "iOS")
    laptop = Laptop("Dell", "XPS 15", 16)

    print(car)
    print(truck.start_engine())
    print(dog.make_sound())
    print(cat)
    print(phone.take_photo())
    print(laptop.turn_on())
