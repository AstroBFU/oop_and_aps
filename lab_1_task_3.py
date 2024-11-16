class Puppy:
    states = ["Болеет", "Выздоравливает", "Здоров"]

    def __init__(self, index):
        self.index = index
        self.state = self.states[0]

    def get_treatment(self):
        if self.state == self.states[0]:
            self.state = self.states[1]
        elif self.state == self.states[1]:
            self.state = self.states[2]
        else:
            return 0
        
    def is_healthy(self):
        if self.state == self.states[2]:
            return "Щенок здоров"
        
    
class Dog:
    def __init__(self, puppy_count):
        self.puppies = [Puppy(i) for i in range(1, puppy_count + 1)]

    def health_all(self):
        for puppy in self.puppies:
            puppy.get_treatment()

    def all_are_healthy(self):
        for puppy in self.puppies:
            if puppy.is_healthy():
                continue
            else:
                return False
        return True
    
    def give_away_all(self):
        if self.all_are_healthy():
            self.puppies.clear()
            print("Все щенки присроены в хорошие руки")
        else:
            print("Не все щенки здоровы")

    
class Vet:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def work(self):
       self.dog.health_all()
       print(f"Все щенки получили лечение от {self.name}")
    def care(self):
        if self.dog.all_are_healthy():
            print("Все щенки здоровы")
            self.dog.give_away_all()
        else:
            print("Есть нездоровые щенки")

    def knowledge_base(self):
        print("База знаний ветеринарской клиники")
        print("1. Проводить регулярные осмотры щенков")
        print("2. Провести лечение нездоровых щенков")
        print("3. Выдать доказательства здоровья")
        print("4. Пристроить щенков в хорошие руки")

    
if __name__ == '__main__':

    dog = Dog(puppy_count=5)

    vet = Vet("Иванов Иван", dog)

    vet.knowledge_base()
    vet.work()
    vet.care()
    dog.give_away_all()
    vet.work()
    vet.care()


