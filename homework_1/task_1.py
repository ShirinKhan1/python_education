class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} says: {self.sound}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Meow")
        self.color = color

    def makesound(self):
        print(f"{self.name} the {self.color} cat says: {self.sound}")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Woof")
        self.color = color

    def makesound(self):
        print(f"{self.name} the {self.color} dog says: {self.sound}")


# Примеры использования
cat = Cat("Whiskers", "black")
dog = Dog("Rex", "brown")

cat.makesound()  # Вывод: Whiskers the black cat says: Meow
dog.makesound()  # Вывод: Rex the brown dog says: Woof