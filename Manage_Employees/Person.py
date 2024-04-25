import math


class Person:
    instances = []

    def __init__(self, name, age):
        self.name = name
        self.level = 1
        self.age = age
        self.job = ""
        self.work_place = None
        Person.instances.append(self)

    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    @staticmethod
    def calc_all():
        Sum = 0
        for instance in Person.instances:
            Sum += instance.calc()
        return Sum
