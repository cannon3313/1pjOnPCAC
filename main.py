class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.score = 0

    def show_info(self):
        print("Name", self.name)
        print("Hp", self.hp)
        print("Score", self.score)



    def set_name(self, new_name):
        self.name = new_name

    def set_hp(self, hp):
        if hp < 100 and hp > 0:
            self.hp = hp
        else:
            print("error hp")

    def set_score(self, score):

        score.score = "set_score"


    def is_alive(self):
        return self.hp > 0

    def damage(self, amount):
        self.hp -= amount

    def add_score(self, amount):
        self.score += amount


from random import randint


player = Player("Barabulka")
player.show_info()

while player.is_alive():
    num = randint(1, 2)
    if num == 1:
        player.damage(randint(1, 20))

        player.add_score(randint(1, 20))

player.show_info()