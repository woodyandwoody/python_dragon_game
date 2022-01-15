from random import randint
import boss
import dragon


class BattleField:
    def __init__(self, field_boss, front_dragons, back_dragons):
        self.field_boss = field_boss
        self.front_dragons = []
        self.back_dragons = []  ## 列表要先定义
        for key in front_dragons:
            self.front_dragons.append(dragon.BattleDragon(key))
        for key in back_dragons:
            self.back_dragons.append(dragon.BattleDragon(key))
        self.dead_dragons = []
        self.win = False
        self.over = False

    def ap(self):
        self.field_boss.ap()
        for key in self.front_dragons:
            key.ap()

    def change_position(self, position):
        temp = self.front_dragons[position]
        self.front_dragons[position] = self.back_dragons[position]
        self.back_dragons[position] = temp

    def battle_filed_info(self):
        message = f"\nBOSS: \t{self.field_boss.health}"
        print(message)
        print(f"Front Line:")
        for key in self.front_dragons:
            print(f"\t{key.info()}")
        print(f"Back Line:")
        for key in self.back_dragons:
            print(f"\t{key.info()}")

    def boss_turn(self):
        if self.field_boss.active():
            print(f"\nBOSS TURN:")
            key = randint(0, len(self.front_dragons) - 1)
            self.front_dragons[key].get_hurt(self.field_boss.attack())

            if not self.front_dragons[key].alive_status():  ## 前排死了吗？
                if self.back_dragons[key].alive_status():
                    self.change_position(key)
                else:  ##前后都挂了就没戏了
                    del self.front_dragons[key]
                    del self.back_dragons[key]
                self.battle_filed_info()

            if not self.front_dragons:
                self.over = True
                return self.over

    def player_choice(self, value, key):
        if value == 2:
            if self.front_dragons[key].skill() < 0:
                for friend_dragon in self.front_dragons:
                    friend_dragon.get_heal(0 - self.front_dragons[key].skill())
            else:
                self.field_boss.get_hurt(self.front_dragons[key].skill())
        elif value == 3 and self.back_dragons[key].alive_status():
            self.change_position(key)  # 不满足要求就执行1
        else:  # value == 1
            self.field_boss.get_hurt(self.front_dragons[key].attack())
        self.front_dragons[key].turn_over()

    def character_turn(self, key):
        self.front_dragons[key].turn_start()  # 写了忘记加，感觉这么写不好

        print(f"\n{self.front_dragons[key].name()}'s turn. ")
        self.battle_filed_info()

        message = f"\nPress 1 or ENTER for attack, 2 skill"
        if self.back_dragons[key].alive_status():
            message += (", 3 change dragon")
        print(message)

    def player_turn(self):
        for key in range(0, len(self.front_dragons) - 1):
            if self.front_dragons[key].active():
                self.character_turn(key)
                while True:
                    try:
                        self.player_choice(int(input()), key)
                    except ValueError:
                        print("Please check your input")
                    else:
                        break

            if self.field_boss.dead:
                self.win = True
                self.over = True
                break
        return self.over
