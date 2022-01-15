HDD_CRITICAL = 100


class Dragon:
    def __init__(self, name: str, health: int, damage: int, skill_damage: int, speed: int, skill_active_punish: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.skill_damage = skill_damage
        self.speed = speed
        self.skill_active_punish = skill_active_punish


class BattleDragon:
    def __init__(self, dragon: Dragon):
        self.action_point = 0
        self.hdd_point = 0
        self.dragon = dragon
        self.health_point = dragon.health
        self.hdd_form = False
        self.alive = True

    def attack(self):
        if self.hdd_form:
            return self.dragon.damage * 2
        else:
            self.hdd_point += 10
            return self.dragon.damage

    def get_hurt(self, enemy_damage):
        self.health_point -= enemy_damage
        print(f"{self.dragon.name.title()} get {enemy_damage} damage.")
        if self.health_point <= 0:
            self.alive = False
            self.health_point = 0
            print(f"{self.dragon.name.title()} is dead.")
            return 0
        self.hdd_point += 20
        return self.health_point

    def skill(self):
        if self.hdd_form:
            return self.dragon.skill_damage * 2
            self.action_point -= self.dragon.skill_active_punish
        else:
            self.hdd_point += 10
            return self.dragon.skill_damage

    def alive_status(self):
        return self.alive

    def turn_start(self):
        if self.hdd_point >= 100:
            self.hdd_form = True
            self.hdd_point = 100
            print(f"{self.dragon.name} has changed to HDD form.")

    def turn_over(self):
        if self.hdd_form:
            self.hdd_point -= 30
            if self.hdd_point <= 0:
                self.hdd_form = False
                print(f"{self.dragon.name} has changed to normal form")

    def active(self):
        # if self.action_point % self.dragon.speed == 0:
        if self.action_point == self.dragon.speed:
            self.action_point = 0
            return True
        else:
            return False

    def ap(self):
        self.action_point += 1

    def info(self):
        if self.alive:
            message = f"{self.dragon.name.title()}: \tHP {self.health_point} \tSTR {self.dragon.damage}"
            if self.hdd_form:
                message += "\tDRAGON FORM!!!"
        else:
            message = f"{self.dragon.name.title()}: DEAD"

        # message += f"HDD\t{self.hdd_point}"

        return message

    def name(self):
        return self.dragon.name.title()

    def get_heal(self, value):
        self.health_point += value
        if self.health_point >= self.dragon.health:
            self.health_point = self.dragon.health
