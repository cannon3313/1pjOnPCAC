import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.job = job
        self.car = car
        self.home = home
        self.gladness = 50

    def get_car(self):
            self.car = Car("audi")

    def get_home(self):
            self.home = House()


    def get_job(self):
        pass


    def work(self):
         self.money += self.job.salary
         self.gladness -= random.randint(1, 10)


    def chill(self):
        self.gladness += random.randint(5, 15)
        self.money -= random.randint(10, 20)

    def clean_home(self):
        pass


    def is_alive(self):
            if self.gladness <= 0:
                print("Depression")
                return  False
            elif self.money < 100:
                print("Bankrupt")
                return False


    def live(self):
        if self.is_alive():
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print ("Bought new car ", self.car.brand)

        if self.job is None:
            self.get_job()
            print("I've got a new job", self.job.job, "witn salary", self.job.salary )

        if self.money <= 0:
            self.work()
            print("go to work")

import random

class Job:
    def __init__(self):
        self.job = random.choice(("developer", "driver", "teacher", "taxi"))
        self.salary = random.randint(100, 200)
class House:
    def __init__(self):
        self.food = 0
        self.mess = 0
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.countHuman = 2
        self.passengers = []

    def add_passenger(self, *args):
        for human in args:
            self.passengers.append(human)

    def show_passengers(self):
        if self.passengers != []:
            print("Model:",self.brand)
            for human in self.passengers:
                print(human.name)
        else:
            print("There are not passengers in car!")

#nick = Human("Nick")
#kate = Human("Kate")
#car = Car("audi")
#car.add_passenger(nick, kate)
#car.show_passengers()