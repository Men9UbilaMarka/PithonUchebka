class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Пример использования

# Создание объекта Singleton
obj1 = Singleton()

# Создание еще одного объекта Singleton
obj2 = Singleton()

# Проверка идентичности объектов
print(obj1 is obj2)  # True