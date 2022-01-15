class Boss:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.dead = False
        self.active_point = 0
        self.speed = speed

    def attack(self):
        return self.damage

    def get_hurt(self, player_damage):
        self.health -= player_damage
        if self.health <= 0:
            self.dead = True
            return 0
        else:
            return self.health

    def active(self):
        if self.active_point % self.speed == 0:
            return True
        else:
            return False

    def ap(self):
        self.active_point += 1
