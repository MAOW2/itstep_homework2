import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.energy = 80
        self.knowledge = 20
        self.happiness = 70
        self.day = 0
    def study(self):
        self.knowledge += random.randint(3, 7)
        self.energy -= random.randint(8, 15)
        self.happiness -= random.randint(2, 6)
        print(f"{self.name} навчається.")
    def work(self):
        salary = random.randint(20, 50)
        self.money += salary
        self.energy -= random.randint(10, 20)
        self.happiness -= random.randint(3, 8)
        print(f"{self.name} працює і заробляє {salary} грн.")
    def rest(self):
        cost = random.randint(10, 30)
        self.money -= cost
        self.energy += random.randint(15, 30)
        self.happiness += random.randint(5, 12)
        print(f"{self.name} відпочиває і витрачає {cost} грн.")
    def live_one_day(self):
        self.day += 1
        print(f"\nДень {self.day}")
        if self.money < 30:
            self.work()
        elif self.energy < 25:
            self.rest()
        elif self.knowledge < self.day // 4:
            self.study()
        else:
            action = random.choice([self.study, self.work, self.rest])
            action()
        self.money -= 5
        self.energy = max(0, min(100, self.energy))
        self.knowledge = max(0, min(100, self.knowledge))
        self.happiness = max(0, min(100, self.happiness))
        print(f"Гроші: {self.money}")
        print(f"Енергія: {self.energy}")
        print(f"Знання: {self.knowledge}")
        print(f"Настрій: {self.happiness}")
    def live_year(self):
        for _ in range(365):
            self.live_one_day()
        print("\nРік завершено!")
        print(f"Студент: {self.name}")
        print(f"Гроші: {self.money}")
        print(f"Енергія: {self.energy}")
        print(f"Знання: {self.knowledge}")
        print(f"Настрій: {self.happiness}")
student = Student("Олексій")
student.live_year()