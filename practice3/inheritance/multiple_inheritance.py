class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Имя:", self.name)


class Worker:
    def __init__(self, job):
        self.job = job

    def info(self):
        print("Работа:", self.job)


class StudentWorker(Person, Worker):  # наследуем от двух классов
    def __init__(self, name, job):
        Person.__init__(self, name)   # вызываем конструктор Person
        Worker.__init__(self, job)    # вызываем конструктор Worker

    def full_info(self):
        print(f"Студент-работник: {self.name}, профессия: {self.job}")


# Пример использования
sw = StudentWorker("Mike", "Developer")
sw.info()        # вызовет метод из Person (по MRO)
print(sw.job)    # доступ к свойству из Worker
sw.full_info()   # собственный метод StudentWorker
